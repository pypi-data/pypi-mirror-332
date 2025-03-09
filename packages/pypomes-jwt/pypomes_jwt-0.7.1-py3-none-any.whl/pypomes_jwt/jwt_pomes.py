import contextlib
import jwt
from flask import Request, Response, request, jsonify
from logging import Logger
from typing import Any, Literal

from .jwt_constants import (
    JWT_ACCESS_MAX_AGE, JWT_REFRESH_MAX_AGE,
    JWT_DEFAULT_ALGORITHM, JWT_DECODING_KEY
)
from .jwt_data import JwtData

# the JWT data object
__jwt_data: JwtData = JwtData()


def jwt_needed(func: callable) -> callable:
    """
    Create a decorator to authenticate service endpoints with JWT tokens.

    :param func: the function being decorated
    """
    # ruff: noqa: ANN003
    def wrapper(*args, **kwargs) -> Response:
        response: Response = jwt_verify_request(request=request)
        return response if response else func(*args, **kwargs)

    # prevent a rogue error ("View function mapping is overwriting an existing endpoint function")
    wrapper.__name__ = func.__name__

    return wrapper


def jwt_assert_access(account_id: str) -> bool:
    """
    Determine whether access for *account_id* has been established.

    :param account_id: the account identification
    :return: *True* if access data exists for *account_id*, *False* otherwise
    """
    return __jwt_data.access_data.get(account_id) is not None


def jwt_set_access(account_id: str,
                   reference_url: str,
                   claims: dict[str, Any],
                   access_max_age: int = JWT_ACCESS_MAX_AGE,
                   refresh_max_age: int = JWT_REFRESH_MAX_AGE,
                   grace_interval: int = None,
                   token_audience: str = None,
                   token_nonce: str = None,
                   request_timeout: int = None,
                   remote_provider: bool = True,
                   logger: Logger = None) -> None:
    """
    Set the data needed to obtain JWT tokens for *account_id*.

    :param account_id: the account identification
    :param reference_url: the reference URL (for remote providers, URL to obtain and validate the JWT tokens)
    :param claims: the JWT claimset, as key-value pairs
    :param access_max_age: access token duration, in seconds
    :param refresh_max_age: refresh token duration, in seconds
    :param grace_interval: optional time to wait for token to be valid, in seconds
    :param token_audience: optional audience the token is intended for
    :param token_nonce: optional value used to associate a client session with a token
    :param request_timeout: timeout for the requests to the reference URL
    :param remote_provider: whether the JWT provider is a remote server
    :param logger: optional logger
    """
    if logger:
        logger.debug(msg=f"Register access data for '{account_id}'")

    # extract the claims provided in the reference URL's query string
    pos: int = reference_url.find("?")
    if pos > 0:
        params: list[str] = reference_url[pos+1:].split(sep="&")
        for param in params:
            claims[param.split("=")[0]] = param.split("=")[1]
        reference_url = reference_url[:pos]

    # register the JWT service
    __jwt_data.add_access(account_id=account_id,
                          reference_url=reference_url,
                          claims=claims,
                          access_max_age=access_max_age,
                          refresh_max_age=refresh_max_age,
                          grace_interval=grace_interval,
                          token_audience=token_audience,
                          token_nonce=token_nonce,
                          request_timeout=request_timeout,
                          remote_provider=remote_provider,
                          logger=logger)


def jwt_remove_access(account_id: str,
                      logger: Logger = None) -> bool:
    """
    Remove from storage the JWT access data for *account_id*.

    :param account_id: the account identification
    :param logger: optional logger
    return: *True* if the access data was removed, *False* otherwise
    """
    if logger:
        logger.debug(msg=f"Remove access data for '{account_id}'")

    return __jwt_data.remove_access(account_id=account_id,
                                    logger=logger)


def jwt_validate_token(errors: list[str] | None,
                       token: str,
                       nature: Literal["A", "R"] = None,
                       logger: Logger = None) -> bool:
    """
    Verify if *token* ia a valid JWT token.

    Raise an appropriate exception if validation failed.

    :param errors: incidental error messages
    :param token: the token to be validated
    :param nature: optionally validate the token's nature ("A": access token, "R": refresh token)
    :param logger: optional logger
    :return: *True* if token is valid, *False* otherwise
    """
    if logger:
        logger.debug(msg=f"Validate JWT token '{token}'")

    err_msg: str | None = None
    try:
        # raises:
        #   InvalidTokenError: token is invalid
        #   InvalidKeyError: authentication key is not in the proper format
        #   ExpiredSignatureError: token and refresh period have expired
        #   InvalidSignatureError: signature does not match the one provided as part of the token
        claims: dict[str, Any] = jwt.decode(jwt=token,
                                            key=JWT_DECODING_KEY,
                                            algorithms=[JWT_DEFAULT_ALGORITHM])
        if nature and "nat" in claims and nature != claims.get("nat"):
            nat: str = "an access" if nature == "A" else "a refresh"
            err_msg = f"Token is not {nat} token"
    except Exception as e:
        err_msg = str(e)

    if err_msg:
        if logger:
            logger.error(msg=err_msg)
        if isinstance(errors, list):
            errors.append(err_msg)
    elif logger:
        logger.debug(msg=f"Token '{token}' is valid")

    return err_msg is None


def jwt_get_tokens(errors: list[str] | None,
                   account_id: str,
                   account_claims: dict[str, Any] = None,
                   logger: Logger = None) -> dict[str, Any]:
    """
    Issue and return the JWT token data associated with *account_id*.

    Structure of the return data:
    {
      "access_token": <jwt-token>,
      "created_in": <timestamp>,
      "expires_in": <seconds-to-expiration>,
      "refresh_token": <jwt-token>
    }

    :param errors: incidental error messages
    :param account_id: the account identification
    :param account_claims: if provided, may supercede registered custom claims
    :param logger: optional logger
    :return: the JWT token data, or *None* if error
    """
    # inicialize the return variable
    result: dict[str, Any] | None = None

    if logger:
        logger.debug(msg=f"Retrieve JWT token data for '{account_id}'")
    try:
        result = __jwt_data.issue_tokens(account_id=account_id,
                                         account_claims=account_claims,
                                         logger=logger)
        if logger:
            logger.debug(msg=f"Data is '{result}'")
    except Exception as e:
        if logger:
            logger.error(msg=str(e))
        if isinstance(errors, list):
            errors.append(str(e))

    return result


def jwt_get_claims(errors: list[str] | None,
                   token: str,
                   logger: Logger = None) -> dict[str, Any]:
    """
    Obtain and return the claims set of a JWT *token*.

    :param errors: incidental error messages
    :param token: the token to be inspected for claims
    :param logger: optional logger
    :return: the token's claimset, or *None* if error
    """
    # initialize the return variable
    result: dict[str, Any] | None = None

    if logger:
        logger.debug(msg=f"Retrieve claims for token '{token}'")

    try:
        reply: dict[str, Any] = jwt.decode(jwt=token,
                                           options={"verify_signature": False})
        if reply.get("nat") in ["A", "R"]:
            result = jwt.decode(jwt=token,
                                key=JWT_DECODING_KEY,
                                algorithms=[JWT_DEFAULT_ALGORITHM])
        else:
            result = reply
    except Exception as e:
        if logger:
            logger.error(msg=str(e))
        if isinstance(errors, list):
            errors.append(str(e))

    return result


def jwt_verify_request(request: Request,
                       logger: Logger = None) -> Response:
    """
    Verify wheher the HTTP *request* has the proper authorization, as per the JWT standard.

    :param request: the request to be verified
    :param logger: optional logger
    :return: *None* if the request is valid, otherwise a *Response* object reporting the error
    """
    # initialize the return variable
    result: Response | None = None

    if logger:
        logger.debug(msg="Validate a JWT token")
    err_msg: str | None = None

    # retrieve the authorization from the request header
    auth_header: str = request.headers.get("Authorization")

    # was a 'Bearer' authorization obtained ?
    if auth_header and auth_header.startswith("Bearer "):
        # yes, extract and validate the JWT token
        token: str = auth_header.split(" ")[1]
        if logger:
            logger.debug(msg=f"Token is '{token}'")
        errors: list[str] = []
        jwt_validate_token(errors=errors,
                           token=token)
        if errors:
            err_msg = "; ".join(errors)
    else:
        # no 'Bearer' found, report the error
        err_msg = "Request header has no 'Bearer' data"

    # log the error and deny the authorization
    if err_msg:
        if logger:
            logger.error(msg=err_msg)
        result = Response(response="Authorization failed",
                          status=401)

    return result


def jwt_claims(token: str = None) -> Response:
    """
    REST service entry point for retrieving the claims of a JWT token.

    Structure of the return data:
    {
      "<claim-1>": <value-of-claim-1>,
      ...
      "<claim-n>": <value-of-claim-n>
    }

    :param token: the JWT token
    :return: a *Response* containing the requested JWT token claims, or reporting an error
    """
    # declare the return variable
    result: Response

    # retrieve the token
    # noinspection PyUnusedLocal
    if not token:
        token = request.values.get("token")
        if not token:
            with contextlib.suppress(Exception):
                token = request.get_json().get("token")

    # has the token been obtained ?
    if token:
        # yes, obtain the token data
        errors: list[str] = []
        token_claims: dict[str, Any] = jwt_get_claims(errors=errors,
                                                      token=token)
        if errors:
            result = Response(response=errors,
                              status=400)
        else:
            result = jsonify(token_claims)
    else:
        # no, report the problem
        result = Response(response="Invalid parameters",
                          status=400)

    return result


def jwt_tokens(service_params: dict[str, Any] = None) -> Response:
    """
    REST service entry point for obtaining or refreshing JWT tokens.

    The requester must send, as parameter *service_params* or in the body of the request:
    {
      "account-id": "<string>"                             - required account identification
      "refresh_token": <string>                            - if refresh is being requested
      "<account-claim-key-1>": "<account-claim-value-1>",  - optional superceding account claims
      ...
      "<account-claim-key-n>": "<account-claim-value-n>"
    }
    if provided, the refresh token will cause a token refresh operation to be carried out.
    Otherwise, a regular token issue operation is carried out, with the optional superceding
    account claims being used (claims currently registered for the account may be overridden).

    Structure of the return data:
    {
      "access_token": <jwt-token>,
      "created_in": <timestamp>,
      "expires_in": <seconds-to-expiration>,
      "refresh_token": <jwt-token>
    }

    :param service_params: the optional JSON containing the request parameters (defaults to JSON in body)
    :return: a *Response* containing the requested JWT token data, or reporting an error
    """
    # declare the return variable
    result: Response

    # retrieve the parameters
    # noinspection PyUnusedLocal
    params: dict[str, Any] = service_params or {}
    if not params:
        with contextlib.suppress(Exception):
            params = request.get_json()
    account_id: str | None = params.pop("account-id", None)
    refresh_token: str | None = params.pop("refresh-token", None)
    err_msg: str | None = None
    token_data: dict[str, Any] | None = None

    # has the account been identified ?
    if account_id:
        # yes, proceed
        if refresh_token:
            errors: list[str] = []
            claims: dict[str, Any] = jwt_get_claims(errors=errors,
                                                    token=refresh_token)
            if errors:
                err_msg = "; ".join(errors)
            elif claims.get("nat") != "R":
                err_msg = "Invalid parameters"
            else:
                params = claims

        if not err_msg:
            try:
                token_data = __jwt_data.issue_tokens(account_id=account_id,
                                                     account_claims=params)
            except Exception as e:
                # token issuing failed
                err_msg = str(e)
    else:
        # no, report the problem
        err_msg = "Invalid parameters"

    if err_msg:
        result = Response(response=err_msg,
                          status=401)
    else:
        result = jsonify(token_data)

    return result

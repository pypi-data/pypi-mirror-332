from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from pypomes_core import (
    APP_PREFIX,
    env_get_str, env_get_bytes, env_get_int, env_get_bool
)
from secrets import token_bytes
from typing import Final

# database specs for token persistence
JWT_DB_ENGINE: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DB_ENGINE")
JWT_DB_HOST: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DB_HOST")
JWT_DB_NAME: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DB_NAME")
JWT_DB_PORT: Final[int] = env_get_int(key=f"{APP_PREFIX}_JWT_DB_PORT")
JWT_DB_USER: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DB_USER")
JWT_DB_PWD: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DB_PWD")

JWT_ROTATE_TOKENS: Final[bool] = False \
    if JWT_DB_ENGINE is None else env_get_bool(key=f"{APP_PREFIX}_JWT_ROTATE_TOKENS",
                                               def_value=False)

# one of HS256, HS512, RSA256, RSA512
JWT_DEFAULT_ALGORITHM: Final[str] = env_get_str(key=f"{APP_PREFIX}_JWT_DEFAULT_ALGORITHM",
                                                def_value="HS256")
# recommended: between 5 min and 1 hour (set to 5 min)
JWT_ACCESS_MAX_AGE: Final[int] = env_get_int(key=f"{APP_PREFIX}_JWT_ACCESS_MAX_AGE",
                                             def_value=300)
# recommended: at least 2 hours (set to 24 hours)
JWT_REFRESH_MAX_AGE: Final[int] = env_get_int(key=f"{APP_PREFIX}_JWT_REFRESH_MAX_AGE",
                                              def_value=86400)

# recommended: allow the encode and decode keys to be generated anew when app starts
__encoding_key: bytes = env_get_bytes(key=f"{APP_PREFIX}_JWT_ENCODE_KEY")
__decoding_key: bytes
if JWT_DEFAULT_ALGORITHM in ["HS256", "HS512"]:
    if not __encoding_key:
        __encoding_key = token_bytes(nbytes=32)
    __decoding_key = __encoding_key
else:
    __decoding_key: bytes = env_get_bytes(key=f"{APP_PREFIX}_JWT_DECODE_KEY")
    if not __encoding_key or not __decoding_key:
        __priv_key: RSAPrivateKey = rsa.generate_private_key(public_exponent=65537,
                                                             key_size=2048)
        __encoding_key = __priv_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                  format=serialization.PrivateFormat.PKCS8,
                                                  encryption_algorithm=serialization.NoEncryption())
        __pub_key: RSAPublicKey = __priv_key.public_key()
        __decoding_key = __pub_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PublicFormat.SubjectPublicKeyInfo)
JWT_ENCODING_KEY: Final[bytes] = __encoding_key
JWT_DECODING_KEY: Final[bytes] = __decoding_key

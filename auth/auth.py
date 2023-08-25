from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from config import SECRET_COOK

cookie_transport = CookieTransport(cookie_name="yes", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_COOK, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

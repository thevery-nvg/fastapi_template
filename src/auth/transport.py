from fastapi_users.authentication import BearerTransport
from fastapi_users.authentication import CookieTransport

bearer_transport = BearerTransport(
    # TODO: update url
    tokenUrl="/api/auth/login",
)

cookie_transport = CookieTransport(cookie_max_age=3600,cookie_name="fastapi_cookie_users")

from fastapi_users.authentication import AuthenticationBackend
from .transport import bearer_transport,cookie_transport
from .strategy import get_database_strategy,get_jwt_strategy


auth_backend2 = AuthenticationBackend(
    name="access_tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
auth_backend = AuthenticationBackend(
    name="access_bearer_jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
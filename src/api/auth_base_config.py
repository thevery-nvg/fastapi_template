from fastapi_users import FastAPIUsers
from .dependencies.backend import auth_backend
from .dependencies.user_manager import get_user_manager
from core.models import User
from core.types.user_id import UserIdType
from fastapi import APIRouter

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

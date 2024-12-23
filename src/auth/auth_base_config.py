from fastapi_users import FastAPIUsers

from .schemas import UserRead, UserCreate
from .dependencies.backend import auth_backend
from .dependencies.user_manager import get_user_manager
from .models import User

from fastapi import APIRouter

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

# \login \logout
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
# \register
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

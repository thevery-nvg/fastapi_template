from fastapi import Depends

from auth.dependencies.users import get_users_db
from auth.user_manager import UserManager


async def get_user_manager(user_db=Depends(get_users_db)):
    yield UserManager(user_db)

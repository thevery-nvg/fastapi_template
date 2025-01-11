from typing import TYPE_CHECKING

from fastapi import Depends

from auth.models import User
from core.models import db_manager

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(session: "AsyncSession" = Depends(db_manager.get_async_session)):
    yield User.get_db(session=session)

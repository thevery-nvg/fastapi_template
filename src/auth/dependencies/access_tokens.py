from typing import TYPE_CHECKING

from fastapi import Depends

from core.models import db_manager
from auth.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
        session: "AsyncSession" = Depends(db_manager.get_async_session)):
    yield AccessToken.get_db(session=session)

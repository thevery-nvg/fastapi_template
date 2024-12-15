from fastapi import APIRouter, Depends

from core.models import db_helper
from src.core.models import User, get_all_users
from src.core.schemas import UserRead
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter()


@user_router.get("/", response_model=list[UserRead])
async def read_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await get_all_users(session=session)

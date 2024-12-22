from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.models import Base
from core.models.mixins.ID_intpk_mixin import IDIntPKMixin


class User(Base, IDIntPKMixin, SQLAlchemyBaseUserTable[int]):
    pass

import logging
from typing import Optional
from fastapi_users import BaseUserManager, IntegerIDMixin
from .models import User
from core.config import settings
from typing import TYPE_CHECKING
from .dependencies.users import get_users_db
from fastapi import Depends
log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from fastapi import Request, Depends


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token:%r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )


async def get_user_manager(user_db=Depends(get_users_db)):
    yield UserManager(user_db)

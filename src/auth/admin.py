import hashlib
import secrets

from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request


from auth.models import User
from core.config import settings


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        is_user_exist = username == settings.admin.username
        if is_user_exist:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        else:
            return False
        if hashed_password == settings.admin.password:
            request.session.update(
                {
                    "token": "b6f2211f8f41a5b58cc13c7a2d05df192b1606c68df7b23907d4ed49bda69d60a28a10ad33e7feea55fc444988b85dec34c7eda8133e6cb4b86b8afda40792f0"
                }
            )
            return True
        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True


authentication_backend = AdminAuth(
    secret_key="a952b3858b0f55efc06945939bbd3b9136c7cc78989234ab4c8c64f3b45988fb2e9b6a1f23e41da540b8f6ca44ef68709c0dadcd268bc1919809b777b59acfa4"
)

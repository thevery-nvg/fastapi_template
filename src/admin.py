from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from auth.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        # Validate username/password credentials
        # And update session
        request.session.update({"token": "kjfdhangoifadnofiuv"})

        return True

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
    secret_key="ladksjfngoieundofvifuandeouivnvoadsiuunfvoidn"
)

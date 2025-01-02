from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse

import uvicorn

from core.config import settings
from core.models import db_helper
from fastapi.responses import ORJSONResponse
from auth import auth_router, users_router

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqladmin import Admin
from auth.admin import UserAdmin, authentication_backend
from auth.users_proxy import fastapi_users_proxy_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    # startup

    # shutdown
    yield
    await db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(auth_router, prefix=settings.prefix.api)
app.include_router(users_router, prefix=settings.prefix.api)
app.include_router(fastapi_users_proxy_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# admin--------------
admin = Admin(app=app, authentication_backend=authentication_backend,
              session_maker=db_helper.session_factory)
admin.add_view(UserAdmin)


# admin--------------


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "xxx": "Вход"})


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )

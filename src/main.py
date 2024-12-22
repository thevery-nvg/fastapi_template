from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from api import api_router, auth_backend
from core.config import settings
from core.models import db_helper
from fastapi.responses import ORJSONResponse
from api.auth_base_config import fastapi_users


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
app.include_router(
    api_router,
    prefix=settings.prefix.api)



if __name__ == '__main__':
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)

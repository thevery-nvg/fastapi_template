from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from core.config import settings
from core.models import db_helper
from fastapi.responses import ORJSONResponse
from auth import auth_router, users_router


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

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )

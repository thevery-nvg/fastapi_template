from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from api import api_router
from core.config import settings
from core.models import db_helper, Base
from fastapi.responses import ORJSONResponse

@asynccontextmanager
async def lifespan(application: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # shutdown
    yield
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
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

from fastapi import FastAPI
import uvicorn
from api import api_router
from core.config import settings

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.prefix.api)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)

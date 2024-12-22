from fastapi import APIRouter
from .auth_base_config import auth_router as auth_router
from .dependencies.backend import auth_backend

api_router = APIRouter()
api_router.include_router(auth_router)
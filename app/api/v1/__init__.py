from fastapi import APIRouter
from .auth import router as auth_router
from .book import router as book_router

api_router = APIRouter()

# Auth endpoints (register, login)
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])

# Book endpoints (CRUD)
api_router.include_router(book_router, tags=["books"])

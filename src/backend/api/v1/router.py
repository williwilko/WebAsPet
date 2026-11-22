from fastapi import APIRouter

from . import users, pets

router = APIRouter()

router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

router.include_router(
    pets.router,
    prefix="/pets",
    tags=["Pets"]
)
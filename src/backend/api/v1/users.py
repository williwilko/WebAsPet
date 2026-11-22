from fastapi import APIRouter

from models.users import User

router = APIRouter()

@router.get('/')
async def index():
    return User('abc', 'wolfgang', 'abc', 'abc', 'anc')
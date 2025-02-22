from fastapi import APIRouter, Depends
from src.core.models.users import User
from src.api.v1.schemas.users import UserList, UserDetail
from src.api.v1.services.users import UserService

router = APIRouter(prefix="/users")


@router.get("")
async def get_users(users: list[User] = Depends(UserService.list)) -> list[UserList]:
    return users


@router.post("/registration")
async def create_user(user: User = Depends(UserService.create)) -> UserDetail:
    return user


@router.post("/verification")
async def verify_user(user: User = Depends(UserService.verify)) -> UserDetail:
    return user

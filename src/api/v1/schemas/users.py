from uuid import UUID
from src.core.base.enums import Role
from pydantic import BaseModel, EmailStr


class UserList(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: Role
    first_name: str | None
    last_name: str | None
    is_verified: bool


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class ConfigDict:
        from_attributes = True


class UserDetail(UserList):
    pass

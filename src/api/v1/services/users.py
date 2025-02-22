import logging
import re

from fastapi import Depends, Body

from src.api.v1.schemas.users import (
    UserCreate,
)
from src.core.database import get_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.base.exceptions import (
    ObjectAlreadyExists,
)
from src.core.repositories.users import UserRepository
from src.core.models.users import User

logger = logging.getLogger("coffee_shop")


class UserService:
    @classmethod
    async def create(
        cls,
        *,
        user_schema: UserCreate = Body(),
        session: AsyncSession = Depends(get_session),
    ) -> User:
        user_dict = user_schema.model_dump()
        username = user_dict.get("username")
        if username is None:
            email = user_dict.get("email")
            username = re.sub(r"[^a-zA-Z\d+]", "", email)
            user_dict["username"] = username
        try:
            user = await UserRepository.create(db=session, values=user_dict)
        except IntegrityError as e:
            logger.exception(f"USER REGISTRATION: {e}")
            raise ObjectAlreadyExists
        await session.commit()
        await session.refresh(user)
        return user

    @classmethod
    async def list(
        cls,
        *,
        # filters: list[_ColumnExpressionArgument[bool]] = [],
        session: AsyncSession = Depends(get_session),
    ) -> list[User]:
        filters = []
        users = await UserRepository.list(filters=filters, db=session)
        return users

    @classmethod
    async def verify(
        cls,
    ):
        pass


# class AuthService:
#     @classmethod
#     async def token(
#         cls,
#         *,
#         otp_data: OtpData = Body(...),
#         session: AsyncSession = Depends(get_session),
#     ) -> dict:
#         user: User = await cls._verify_auth_code(
#             otp_code=otp_data.otp_code, session=session
#         )
#         username: str | None = user.username
#         user_id: UUID = user.id

#         # Get tokens
#         payload = {"sub": username, "user_id": str(user_id)}
#         tokens = JWTToken.tokens(payload=payload)
#         return {"tokens": tokens}

#     @classmethod
#     async def refresh(
#         cls,
#         *,
#         refresh_token: RefreshToken = Body(...),
#     ) -> dict:
#         try:
#             # Decode the refresh token
#             payload = JWTToken.decode_jwt(
#                 token=refresh_token.refresh,
#             )

#             if payload.get("user_id") is None:
#                 raise TokenInvalid

#         except jwt.ExpiredSignatureError:
#             raise TokenExpired
#         except jwt.PyJWTError:
#             raise TokenInvalid

#         # Get tokens
#         tokens = JWTToken.tokens(payload=payload)
#         return {"tokens": tokens}

#     @classmethod
#     async def _verify_auth_code(cls, *, otp_code: int, session: AsyncSession) -> User:
#         filters = [
#             Code.value == otp_code,
#             Code.expiry >= datetime.now(timezone.utc),
#             Code.is_used == False,  # noqa E712
#         ]
#         codes = await CodeRepository.list(db=session, filters=filters)

#         if len(codes) == 0:
#             raise CodeInvalidOrExpired

#         code = codes[0]
#         return code.user

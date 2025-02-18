from sqlalchemy import insert, select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql._typing import _ColumnExpressionArgument
from src.core.models.users import User


class UserRepository:
    @classmethod
    async def add(cls, *, db: AsyncSession, values: dict) -> User:
        stmt = insert(User).values(**values).returning(User)
        result = await db.execute(stmt)
        return result.scalar_one()

    @classmethod
    async def list(
        cls,
        *,
        db: AsyncSession,
        filters: list[_ColumnExpressionArgument[bool]] = [],
    ) -> list[User]:
        query = select(User).where(and_(*filters))
        result = await db.execute(query)
        return result.scalars().all()

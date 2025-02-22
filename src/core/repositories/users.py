from sqlalchemy import insert, select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql._typing import _ColumnExpressionArgument
from src.core.models.users import User


class UserRepository:
    @classmethod
    async def create(
        cls,
        *,
        values: dict,
        db: AsyncSession,
    ) -> User:
        stmt = insert(User).values(**values).returning(User)
        result = await db.execute(stmt)
        return result.scalar_one()

    @classmethod
    async def list(
        cls,
        *,
        filters: list[_ColumnExpressionArgument[bool]] = [],
        db: AsyncSession,
    ) -> list[User]:
        filters = []
        query = select(User).where(and_(True, *filters))
        result = await db.execute(query)
        return result.scalars().all()

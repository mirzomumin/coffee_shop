from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from src.config import settings


async_engine = create_async_engine(settings.DB_URL)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

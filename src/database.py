from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from src.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
DATABASE_PARAMS = {"echo": True,}

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, **DATABASE_PARAMS
)


class Base(DeclarativeBase):
    pass


async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
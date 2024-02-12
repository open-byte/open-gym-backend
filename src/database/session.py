from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from config.settings import get_settings

_settings_app = get_settings()

async_engine = create_async_engine(_settings_app.database_url, echo=True, future=True)


async def get_session() -> AsyncSession:  # type: ignore
    """
    Get an asynchronous session for database operations.

    Returns:
        AsyncSession: An asynchronous session object.

    """
    async_session = sessionmaker(
        bind=async_engine,  # type: ignore
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session

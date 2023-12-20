import uuid

from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column
)

from src.services.db.app.config import db_settings

async_engine = create_async_engine(
    url=db_settings.db.DATABASE_URL_asyncpg,
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine, class_=AsyncSession)


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__.lower()
        if "model" in name:
            return name.replace("model", "")

    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4
    )


async def get_async_session():
    async with async_session_factory() as async_session:
        yield async_session

from __future__ import annotations
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate

if TYPE_CHECKING:
    from src.domain.entities.profile import ProfileModel


class UserModel(SQLAlchemyBaseUserTable[UUID], BaseModel):

    id: Mapped[short_annotate.uuidpk]
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str]
    is_online: Mapped[bool]

    profile: Mapped["ProfileModel"] = relationship(
        back_populates="user"
    )

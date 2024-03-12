import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    declared_attr,
    mapped_column,
    relationship
)

if TYPE_CHECKING:
    from src.domain.entities import UserModel


class UserRelationMixin:

    _user_id_unique: bool = False
    _user_id_nullable: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[uuid.UUID]:
        return mapped_column(
            UUID, ForeignKey("user.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable
        )

    @declared_attr
    def user(cls) -> Mapped["UserModel"]:
        return relationship(
            "UserModel", back_populates=cls._user_back_populates
        )

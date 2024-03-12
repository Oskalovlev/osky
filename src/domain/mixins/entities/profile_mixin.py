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
    from src.domain.entities import ProfileModel


class ProfileRelationMixin:

    _profile_id_unique: bool = False
    _profile_id_nullable: bool = False
    _profile_back_populates: str | None = None

    @declared_attr
    def profile_id(cls) -> Mapped[uuid.UUID]:
        return mapped_column(
            UUID, ForeignKey("profile.id"),
            unique=cls._profile_id_unique,
            nullable=cls._profile_id_nullable
        )

    @declared_attr
    def profile(cls) -> Mapped["ProfileModel"]:
        return relationship(
            "ProfileModel", back_populates=cls._profile_back_populates
        )

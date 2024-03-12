import uuid
from typing import TYPE_CHECKING, Annotated

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.domain.entities.base_model import BaseUUIDModel
from src.domain.mixins.entities import UserRelationMixin
if TYPE_CHECKING:
    from src.domain.entities import PublicationModel


class ProfileModel(UserRelationMixin, BaseUUIDModel):

    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    phone: Mapped[str | None]
    telegram: Mapped[str | None]
    bio: Mapped[str | None]
    followers: Mapped[list[uuid.UUID]] = mapped_column(
        UUID, ForeignKey("user.id", ondelete="SET NULL")
    )
    following: Mapped[list[uuid.UUID]] = mapped_column(
        UUID, ForeignKey("user.id", ondelete="SET NULL")
    )

    publications: Mapped["PublicationModel"] = relationship(
        back_populates="publisher"
    )
    avatar: Mapped[int] = mapped_column(ForeignKey("avatar.id"), unique=True)

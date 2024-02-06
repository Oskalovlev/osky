import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate
from src.domain.mixins.entities import UserRelationMixin
if TYPE_CHECKING:
    from src.domain.entities.user.avatar import AvatarModel


class ProfileModel(UserRelationMixin, BaseModel):
    _user_id_unique = True
    _user_back_populates = "profile"

    id: Mapped[short_annotate.intpk]
    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    avatar: Mapped["AvatarModel"] = relationship(back_populates="profile")
    phone: Mapped[str | None]
    telegram: Mapped[str | None]
    followers: Mapped[list[uuid.UUID]] = mapped_column(
        UUID, ForeignKey("user.id", ondelete="SET NULL")
    )
    following: Mapped[list[uuid.UUID]] = mapped_column(
        UUID, ForeignKey("user.id", ondelete="SET NULL")
    )

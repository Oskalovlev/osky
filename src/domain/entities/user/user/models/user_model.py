from __future__ import annotations
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.entities.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from src.domain.entities.user.profile import ProfileModel


class UserModel(SQLAlchemyBaseUserTableUUID, BaseUUIDModel):

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_online: Mapped[bool]

    profile: Mapped["ProfileModel"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return (
            f"User id: {self.id!r},"
            f"Username: {self.username!r},"
            f"Email: {self.email!r}"
        )

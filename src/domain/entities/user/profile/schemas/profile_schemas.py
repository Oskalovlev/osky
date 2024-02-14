from __future__ import annotations

from typing import TYPE_CHECKING, Optional

# from pydantic_extra_types.phone_numbers import PhoneNumber

from src.domain.entities.base_schema import PydanticBaseSchema
from src.domain.mixins.entities.user_mixins import UserRelationMixin

if TYPE_CHECKING:
    from src.domain.entities.user import UserReadSchema
    from src.domain.entities.user.avatar import AvatarSchema


class TagSchema(PydanticBaseSchema):
    id: int
    name: str


class ProfileSchema(PydanticBaseSchema):

    id: int
    # user: int
    first_name: str
    last_name: str
    # avatar: "AvatarSchema"
    phone: str
    telegram: str
    # followers: list["ProfileSchema"]
    # followings: list["ProfileSchema"]

    class Config:
        from_attributes = True

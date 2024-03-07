# from __future__ import annotations

# from typing import TYPE_CHECKING

from src.domain.entities.base_schema import PydanticBaseSchema

# if TYPE_CHECKING:
    # from src.domain.entities.user import UserReadSchema
    # from src.domain.entities.user.avatar import AvatarSchema


class TagSchema(PydanticBaseSchema):
    id: int
    name: str


class ProfileSchema(PydanticBaseSchema):

    id: int
    user: int
    first_name: str
    last_name: str
    phone: str
    bio: str
    telegram: str
    followers: list[str]
    followings: list[str]

    avatar: str

    class Config:
        from_attributes = True

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

# from pydantic_extra_types.phone_numbers import PhoneNumber

from src.domain.entities.base_schema import PydanticBaseSchema

if TYPE_CHECKING:
    from src.domain.entities.user import UserOutSchema


class TagSchema(PydanticBaseSchema):
    id: int
    name: str


class ProfileSchem(PydanticBaseSchema):
    id: int
    user: "UserOutSchema"
    avatar: Optional[str]
    phone: str
    telegram: str
    followers: Optional[list["ProfileSchem"]]
    followings: Optional[list["ProfileSchem"]]

    class Config:
        from_attributes = True

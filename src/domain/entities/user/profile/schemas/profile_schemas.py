import uuid
from typing import Annotated
from annotated_types import MaxLen, MinLen

from src.domain.entities.base_schema import (
    PydanticBaseSchema, PydanticIntIDSchema, PydanticUUIDSchema
)


class TagSchema(PydanticIntIDSchema):

    name: str


class ProfileInSchema(PydanticBaseSchema):

    user: uuid.UUID
    first_name: Annotated[str, MinLen(2), MaxLen(40)]
    last_name: Annotated[str, MinLen(2), MaxLen(40)]
    phone: str
    bio: str
    telegram: str
    followers: list[str]
    followings: list[str]

    avatar: str

    class Config:
        from_attributes = True


class ProfileOutSchema(ProfileInSchema, PydanticUUIDSchema):

    pass

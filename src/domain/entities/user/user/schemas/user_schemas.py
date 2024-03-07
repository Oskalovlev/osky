from uuid import UUID
from typing import Annotated
from annotated_types import MaxLen, MinLen

from fastapi_users import schemas
from pydantic import EmailStr

from src.domain.entities.base_schema import PydanticBaseSchema


class UserBaseSchema(PydanticBaseSchema):

    username: Annotated[str, MinLen(4), MaxLen(20)]
    first_name: Annotated[str, MinLen(2), MaxLen(40)]
    last_name: Annotated[str, MinLen(2), MaxLen(40)]
    email: EmailStr
    is_online: bool
    profile: str


class UserReadSchema(UserBaseSchema, schemas.BaseUser[UUID]):

    pass

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema, schemas.BaseUserCreate):

    pass


class UserUpdateSchema(UserBaseSchema, schemas.BaseUserUpdate):

    pass

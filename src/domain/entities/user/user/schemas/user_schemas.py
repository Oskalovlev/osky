from uuid import UUID
from typing import Annotated, TYPE_CHECKING
from annotated_types import MaxLen, MinLen

from fastapi_users import schemas
from pydantic import EmailStr

from src.domain.entities.base_schema import PydanticBaseSchema

if TYPE_CHECKING:
    from src.domain.entities import ProfileOutSchema


class UserBaseSchema(PydanticBaseSchema):

    username: Annotated[str, MinLen(4), MaxLen(20)]
    email: EmailStr
    is_online: bool
    profile: "ProfileOutSchema"


class UserReadSchema(UserBaseSchema, schemas.BaseUser[UUID]):
    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema, schemas.BaseUserCreate):

    pass


class UserUpdateSchema(UserBaseSchema, schemas.BaseUserUpdate):

    pass

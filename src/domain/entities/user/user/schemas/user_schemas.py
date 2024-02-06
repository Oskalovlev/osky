import uuid
from typing import Annotated

from annotated_types import MaxLen, MinLen
from fastapi_users import schemas
from pydantic import UUID4, EmailStr

from src.domain.entities.user.profile import ProfileSchem


class UserBaseSchema(schemas.BaseUser[uuid.UUID]):
    username: Annotated[str, MinLen(3), MaxLen(35)]
    first_name: str
    last_name: str
    email: EmailStr


class UserInSchema(UserBaseSchema):
    password: str


class UserOutSchema(UserBaseSchema):
    id: UUID4
    profile: "ProfileSchem"
    is_online: bool


class UserDBSchema(UserBaseSchema):
    hashed_password: str

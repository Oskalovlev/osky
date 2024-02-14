import uuid
from typing import Annotated

from annotated_types import MaxLen, MinLen
from fastapi_users import schemas
from pydantic import EmailStr, ConfigDict

from src.domain.entities.base_schema import PydanticBaseSchema

# if TYPE_CHECKING:
#     from src.domain.entities.user import ProfileSchema


# class UserInSchema(PydanticBaseSchema):

#     username: Annotated[str, MinLen(3), MaxLen(35)]
#     email: EmailStr
#     password: str
#     confirm_password: str
#     is_online: bool


# class UserOutSchema(PydanticBaseSchema):

#     username: Annotated[str, MinLen(3), MaxLen(35)]
#     email: EmailStr
#     is_online: bool
#     model_config = ConfigDict(from_attributes=True)


class UserReadSchema(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreateSchema(schemas.BaseUserCreate):
    pass


class UserUpdateSchema(schemas.BaseUserUpdate):
    pass

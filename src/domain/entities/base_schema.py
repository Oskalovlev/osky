import uuid

from pydantic import BaseModel


class PydanticBaseSchema(BaseModel):

    pass


class PydanticUUIDSchema(BaseModel):

    id: uuid.UUID


class PydanticIntIDSchema(BaseModel):

    id: int

from datetime import date

from src.domain.entities.base_schema import (
    PydanticBaseSchema, PydanticUUIDSchema
)


class PostSchema(PydanticBaseSchema, PydanticUUIDSchema):

    body: str
    created_at: date

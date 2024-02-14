from datetime import date

from pydantic import UUID4

from src.domain.entities.base_schema import PydanticBaseSchema


class PostSchema(PydanticBaseSchema):

    id: UUID4
    body: str
    created_at: date

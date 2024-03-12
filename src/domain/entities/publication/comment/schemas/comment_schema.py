import uuid

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import ConfigDict

from src.domain.entities.base_schema import (
    PydanticBaseSchema, PydanticIntIDSchema
)
if TYPE_CHECKING:
    # from src.domain.entities.user import ProfileOutSchema
    from src.domain.entities.publication.files import (
        # MusicSchema, ImageSchema, PdfSchema,
        FilesSchema
    )


class CommentBaseSchema(PydanticBaseSchema):

    user: uuid.UUID
    body: str
    likes: int
    created_at: datetime
    files: list["FilesSchema"]

    # music_id: "MusicSchema"
    # image_id: "ImageSchema"
    # pdf_id: "PdfSchema"


class CommentCreateSchema(PydanticBaseSchema):

    pass


class CommentReadSchema(CommentCreateSchema, PydanticIntIDSchema):

    pass


class CommentUpdateSchema(CommentReadSchema):

    user: uuid.UUID = None
    body: str = None
    likes: int = None
    created_at: datetime = None
    files: list["FilesSchema"] = None


class CommentDeleteSchema(CommentReadSchema):

    pass


class CommentDBSchema(CommentBaseSchema, PydanticIntIDSchema):

    model_config = ConfigDict(from_attributes=True)

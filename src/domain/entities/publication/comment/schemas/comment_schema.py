from datetime import datetime

from pydantic import UUID4

from src.domain.entities.base_schema import PydanticBaseSchema
from src.domain.entities.user import ProfileSchema
from src.domain.entities.publication.files import (
    # MusicSchema, ImageSchema, PdfSchema,
    FilesSchema
)


class CommentSchema(PydanticBaseSchema):

    id: UUID4
    user: "ProfileSchema"
    body: str
    likes: int
    created_at: datetime
    files: list["FilesSchema"]

    # music_id: "MusicSchema"
    # image_id: "ImageSchema"
    # pdf_id: "PdfSchema"

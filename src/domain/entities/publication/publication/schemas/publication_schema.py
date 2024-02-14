from pydantic import UUID4

from src.domain.entities.base_schema import PydanticBaseSchema
from src.domain.entities.publication.comment import CommentSchema
from src.domain.entities.publication.post import PostSchema
from src.domain.entities.user.profile import ProfileSchema
from src.domain.entities.publication.files import (
    MusicSchema, ImageSchema, PdfSchema
)


class PublicationSchema(PydanticBaseSchema):

    id: UUID4
    post: "PostSchema"
    comments: list["CommentSchema"]
    publisher: "ProfileSchema"
    is_favorites: bool

    music_id: "MusicSchema"
    image_id: "ImageSchema"
    pdf_id: "PdfSchema"

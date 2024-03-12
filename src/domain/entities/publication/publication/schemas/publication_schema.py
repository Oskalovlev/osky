from typing import TYPE_CHECKING

from pydantic import ConfigDict

from src.domain.entities.base_schema import (
    PydanticBaseSchema, PydanticUUIDSchema
)
if TYPE_CHECKING:
    from src.domain.entities.publication import CommentReadSchema
    from src.domain.entities.publication.post import PostSchema
    from src.domain.entities.user.profile import ProfileOutSchema
    from src.domain.entities.publication.files import (
        MusicSchema, ImageSchema, PdfSchema
    )


class PublicationBaseSchema(PydanticBaseSchema):

    post: "PostSchema"
    comments: list["CommentReadSchema"]
    publisher: "ProfileOutSchema"
    is_favorites: bool

    # music_id: "MusicSchema"
    # image_id: "ImageSchema"
    # pdf_id: "PdfSchema"


class PublicationCreateSchema(PublicationBaseSchema):

    pass


class PublicationReadSchema(PublicationCreateSchema, PydanticUUIDSchema):
    pass


class PublicationUpdateSchema(PublicationReadSchema):

    post: "PostSchema" = None
    comments: list["CommentReadSchema"] = None
    publisher: "ProfileOutSchema" = None
    is_favorites: bool = None

    music_id: "MusicSchema" = None
    image_id: "ImageSchema" = None
    pdf_id: "PdfSchema" = None


class PublicationDeleteSchema(PublicationReadSchema):
    pass


class PublicationDBSchema(PublicationReadSchema):

    model_config = ConfigDict(from_attributes=True)

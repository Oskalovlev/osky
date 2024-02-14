from src.domain.entities.base_schema import PydanticBaseSchema
from src.domain.entities.publication.files import (
    MusicSchema, ImageSchema, PdfSchema
)


class FilesSchema(PydanticBaseSchema):

    music_id: "MusicSchema"
    image_id: "ImageSchema"
    pdf_id: "PdfSchema"

from src.domain.entities.base_schema import PydanticIntIDSchema
from src.domain.entities.publication.files import (
    MusicSchema, ImageSchema, PdfSchema
)


class FilesSchema(PydanticIntIDSchema):

    music_id: "MusicSchema"
    image_id: "ImageSchema"
    pdf_id: "PdfSchema"

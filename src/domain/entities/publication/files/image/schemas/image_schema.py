from src.domain.entities.base_schema import PydanticBaseSchema


class ImageSchema(PydanticBaseSchema):

    id: int
    file_name: str
    file_data: bytes

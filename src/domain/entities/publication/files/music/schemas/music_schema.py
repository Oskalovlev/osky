from src.domain.entities.base_schema import PydanticBaseSchema


class MusicSchema(PydanticBaseSchema):

    id: int
    file_name: str
    file_data: bytes

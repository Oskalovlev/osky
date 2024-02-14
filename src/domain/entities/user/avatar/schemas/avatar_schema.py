from src.domain.entities.base_schema import PydanticBaseSchema


class AvatarSchema(PydanticBaseSchema):

    id: int
    file_name: str
    file_data: bytes

from src.domain.entities.base_schema import PydanticIntIDSchema


class AvatarSchema(PydanticIntIDSchema):

    file_name: str
    file_data: bytes

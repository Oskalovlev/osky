from sqlalchemy.orm import Mapped

from src.domain.entities.base_model import BaseIntIDModel


class ImageModel(BaseIntIDModel):

    file_name: Mapped[str]
    file_data: Mapped[str]

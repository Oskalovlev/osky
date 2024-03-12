from sqlalchemy.orm import Mapped

from src.domain.entities.base_model import BaseIntIDModel
from src.domain.entities.short_annotate import short_annotate


class PdfModel(BaseIntIDModel):

    file_name: Mapped[str]
    file_data: Mapped[str]

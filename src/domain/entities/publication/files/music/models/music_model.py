from sqlalchemy.orm import Mapped

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate


class MusicModel(BaseModel):

    id: Mapped[short_annotate.intpk]
    file_name: Mapped[str]
    file_data: Mapped[str]

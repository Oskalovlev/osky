from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseModel


class FilesModel(BaseModel):

    music_id: Mapped[int] = mapped_column(
        ForeignKey("music.id", ondelete="SET NULL")
    )
    image_id: Mapped[int] = mapped_column(
        ForeignKey("image.id", ondelete="SET NULL")
    )
    pdf_id: Mapped[int] = mapped_column(
        ForeignKey("pdf.id", ondelete="SET NULL")
    )

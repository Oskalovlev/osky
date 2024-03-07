import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate


class PublicationModel(BaseModel):

    post: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("post.id", ondelete="CASCADE")
    )
    comment: Mapped[list[uuid.UUID]] = mapped_column(
        UUID, ForeignKey("comment.id", ondelete="SET NULL")
    )
    publisher: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("user.id", ondelete="CASCADE")
    )
    is_favorites: Mapped[bool]

    music_id: Mapped[int] = mapped_column(
        ForeignKey("music.id", ondelete="SET NULL")
    )
    image_id: Mapped[int] = mapped_column(
        ForeignKey("image.id", ondelete="SET NULL")
    )
    pdf_id: Mapped[int] = mapped_column(
        ForeignKey("pdf.id", ondelete="SET NULL")
    )

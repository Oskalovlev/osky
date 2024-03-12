import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseIntIDModel


class PublicationModel(BaseIntIDModel):

    post: Mapped[int] = mapped_column(
        ForeignKey("post.id", ondelete="CASCADE")
    )
    comment: Mapped[list[int]] = mapped_column(
        ForeignKey("comment.id", ondelete="SET NULL")
    )
    publisher: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("profile.id", ondelete="CASCADE")
    )
    is_favorites: Mapped[bool]

    # music_id: Mapped[int] = mapped_column(
    #     ForeignKey("music.id", ondelete="SET NULL")
    # )
    # image_id: Mapped[int] = mapped_column(
    #     ForeignKey("image.id", ondelete="SET NULL")
    # )
    # pdf_id: Mapped[int] = mapped_column(
    #     ForeignKey("pdf.id", ondelete="SET NULL")
    # )

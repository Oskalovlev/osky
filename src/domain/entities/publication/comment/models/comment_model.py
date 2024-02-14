from datetime import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate


class CommentModel(BaseModel):

    id: Mapped[short_annotate.uuidpk]
    user: Mapped[int] = mapped_column(
        ForeignKey("profile.id", ondelete="CASCADE")
    )
    body: Mapped[str]
    likes: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    fiels: Mapped[list[int]] = mapped_column(
        ForeignKey("files.id", ondelete="SET NULL")
    )

    # music_id: Mapped[int] = mapped_column(
    #     ForeignKey("music.id", ondelete="SET NULL")
    # )
    # image_id: Mapped[int] = mapped_column(
    #     ForeignKey("image.id", ondelete="SET NULL")
    # )
    # pdf_id: Mapped[int] = mapped_column(
    #     ForeignKey("pdf.id", ondelete="SET NULL")
    # )

from datetime import date

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseModel
from src.domain.entities.short_annotate import short_annotate


class PostModel(BaseModel):

    id: Mapped[short_annotate.uuidpk]
    body: Mapped[str]
    crated_at: Mapped[date] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

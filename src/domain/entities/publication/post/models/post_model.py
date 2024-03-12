from datetime import date

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.base_model import BaseIntIDModel


class PostModel(BaseIntIDModel):

    body: Mapped[str]
    crated_at: Mapped[date] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

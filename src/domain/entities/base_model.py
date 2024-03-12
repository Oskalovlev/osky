from sqlalchemy.orm import Mapped

from src.domain.entities.short_annotate import short_annotate
from src.services.database.app.database import Base


# class BaseModel(Base):

#     __abstract__ = True


class BaseUUIDModel(Base):

    __abstract__ = True

    id: Mapped[short_annotate.uuidpk]


class BaseIntIDModel(Base):

    __abstract__ = True

    id: Mapped[short_annotate.intpk]

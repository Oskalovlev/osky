from src.services.db.app.database import Base


class BaseModel(Base):

    __abstract__ = True

from src.domain.entities import UserModel as User
from src.services.db.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):

    pass


user_repository = UserRepository(User)

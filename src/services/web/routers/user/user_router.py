import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.db.app.database import get_async_session
from src.services.db.repository import user_repository
from src.domain.entities.user import UserModel as User
from src.domain.entities.user import UserReadSchema, UserCreateSchema, UserUpdateSchema

router = APIRouter()


@router.get(
    "/",
    response_model=UserReadSchema,
    response_model_exclude_none=True
)
async def get_multi(
    users: UserReadSchema,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    """Получеине пользователей."""
    get_users = await user_repository.get_multi_users(users, session)
    return get_users


@router.post(
    "/",
    response_model=UserCreateSchema,
    response_model_exclude_none=True
)
async def create(
    user: UserCreateSchema,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    """Создание пользователя."""
    new_user = await user_repository.create_user(user, session)
    return new_user


@router.patch(
    "/{user_id}",
    response_model=UserUpdateSchema,
    response_model_exclude_none=True
)
async def update(
    user: UserUpdateSchema,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    """Обновление пользователя."""
    update_user = await user_repository.update_user(user, session)
    return update_user


@router.delete(
    '/{user_id}',
    deprecated=True
)
def delete_user(user_id: uuid.UUID):
    """Не удалять, деактивировать."""

    raise HTTPException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail="Удаление пользователей запрещено!"
    )

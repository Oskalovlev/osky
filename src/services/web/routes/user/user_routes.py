import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.services.db.app.database import get_async_session
from src.services.db.repository import user_repository
from src.domain.entities import UserModel as User
from src.domain.entities import UserInSchema, UserOutSchema, UserDBSchema


router = APIRouter(prefix="/user", tags=["user"])


@router.get(
    "/",
    response_model=UserDBSchema,
    response_model_exclude_none=True
)
async def get(
    users: UserOutSchema,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    """Получеине пользователей."""
    get_users = await user_repository.get_multi(users, session)
    return get_users


@router.post(
    "/",
    response_model=UserDBSchema,
    response_model_exclude_none=True
)
async def create(
    user: UserInSchema,
    session: AsyncSession = Depends(get_async_session)
) -> UserInSchema:
    """Создание пользователя."""
    new_user = await user_repository.create(user, session)
    return new_user


@router.patch(
    "/{user_id}",
    response_model=UserDBSchema,
    response_model_exclude_none=True
)
async def update(
    user: UserOutSchema,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    """Обновление пользователя."""
    update_user = await user_repository.update(user, session)
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

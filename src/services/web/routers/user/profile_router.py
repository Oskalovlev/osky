# import uuid

from fastapi import (
    APIRouter,
    Depends,
    # HTTPException, status
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.database.app.database import get_async_session
from src.services.database.repository import profile_repository
from src.domain.entities.user import ProfileModel as Profile
from src.domain.entities.user import ProfileSchema

router = APIRouter()


@router.get(
    "/",
    response_model=ProfileSchema,
    response_model_exclude_none=True
)
async def get_user_profile(
    profile: ProfileSchema,
    session: AsyncSession = Depends(get_async_session)
) -> Profile:
    """Получение профиля пользователя."""
    get_profile = await profile_repository.get_profile_by_id(profile, session)
    return get_profile

import uuid

from sqlalchemy import (
    delete,
    select,
    update
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities import ProfileModel as Profile, ProfileSchema


class ProfileRepository:

    @staticmethod
    async def get_multi_profiles(
        session: AsyncSession
    ) -> list[Profile]:
        db_profiles = await session.execute(select(Profile))
        return db_profiles.scalars().all()

    @staticmethod
    async def get_profile_by_id(
        profile_id: uuid.UUID,
        session: AsyncSession,
    ) -> Profile:
        db_user = await session.execute(
            select(Profile).where(Profile.id == profile_id)
        )
        db_user = db_user.scalars().first()
        return db_user

    @staticmethod
    async def create_user(
        profile: ProfileSchema,
        session: AsyncSession
    ) -> Profile:
        new_user = profile.model_dump()
        get_new_profile = Profile(**new_user)
        session.add(get_new_profile)
        await session.commit()
        await session.refresh(get_new_profile)
        return get_new_profile

    @staticmethod
    async def update_user(
        profile_id: uuid.UUID,
        session: AsyncSession,
        **kwargs
    ) -> Profile:
        update_user = update(Profile).where(
            Profile.id == profile_id
        ).values(kwargs)
        await session.execute(update_user)

    @staticmethod
    async def delete_user(
        profile_id: uuid.UUID,
        session: AsyncSession
    ) -> None:
        delete_user = delete(Profile).where(Profile.id == profile_id)
        await session.execute(delete_user)

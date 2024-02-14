from fastapi import APIRouter

from src.services.web.routers import user_router
from src.services.web.routers import profile_router

main_router = APIRouter()

main_router.include_router(
    user_router, prefix="/user", tags=["User"]
)
main_router.include_router(
    profile_router, prefix="/profile", tags=["profile"]
)
# main_router.include_router(
#     publication_router, prefix="/publicication", tags=["Publicication"]
# )

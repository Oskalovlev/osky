from fastapi import FastAPI

from src.services.web.config import app_settings as settings
from src.services.web.server import Server


def create_app(_=None) -> FastAPI:
    app = FastAPI(
        title=settings.app.APP_TITLE,
        description=settings.app.DESCRIPTION
    )

    return Server(app).get_app()

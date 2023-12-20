from pydantic_settings import BaseSettings, SettingsConfigDict

from src.services.settings_schemas import DatabaseConfig


class DBSettings(BaseSettings):

    db: DatabaseConfig

    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", extra="ignore"
    )


db_settings = DBSettings()

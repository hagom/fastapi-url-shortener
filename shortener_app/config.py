# shortener_app/config.py

from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    SETTINGS  VARIABLE | ENVIRONMENT VARIABLE | VALUE 

    env_name            ENV_NAME                Name of your current environment
    base_url            BASE_URL                Domain of your app
    db_url              DB_URL                  Address of your database
    """
    env_name: str = "Local"
    base_url: str = "http:localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Carga de configuracion: {settings.env_name}")
    return settings

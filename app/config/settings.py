import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    
    APP_NAME: str = os.environ.get("APP_NAME", "Authentication")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "secret")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", 'postgres')
    DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
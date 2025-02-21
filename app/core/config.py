from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Smart Grid API"

    # CORS settings
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # In production, replace with specific origins

    model_config = SettingsConfigDict(case_sensitive=True)


# Create settings instance
settings = Settings()

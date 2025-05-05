import os
from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn

class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Book Management Service"
    
    # Security
    SECRET_KEY: str = Field(default="your-secret-key-for-dev", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: PostgresDsn = Field(
        default="postgresql://postgres:postgres@localhost:5432/book_management",
        env="DATABASE_URL"
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
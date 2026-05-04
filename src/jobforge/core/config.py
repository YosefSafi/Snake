from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///jobforge.db"
    LOG_LEVEL: str = "INFO"
    TARGET_ROLES: str = ""
    TARGET_LOCATION: str = "Remote"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

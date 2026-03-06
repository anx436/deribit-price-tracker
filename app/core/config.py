from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    DATABASE_URL: str
    # REDIS_URL: str
    RABBITMQ_URL: str

    DERIBIT_BASE_URL: str = "https://www.deribit.com/api/v2"

settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    DERIBIT_BASE_URL: str = "https://www.deribit.com/api/v2"

    class Config:
        env_file = ".env"

settings = Settings()

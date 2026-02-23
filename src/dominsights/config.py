from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dominion_username: str
    dominion_password: str
    account_number: str
    meter_number: str

    token_file: Path
    cookie_file: Path
    database_path: Path
    price_per_kwh: float = 0.15

    class Config:
        env_file = ".env"


settings = Settings()

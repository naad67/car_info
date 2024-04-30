import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(override=True)


class Settings(BaseSettings):
    DB_NAME: str = os.getenv("DB_NAME", "car_database")
    DB_HOST: str = os.getenv("DB_HOST", "db")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASS: str = os.getenv("DB_PASS", "root")

    @property
    def database_settings(self):
        return {
            "database": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASS,
            "host": self.DB_HOST,
            "port": self.DB_PORT,
        }

    @property
    def database_url(self) -> str:
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def database_migration_url(self) -> str:
        return "postgresql://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )


settings = Settings()
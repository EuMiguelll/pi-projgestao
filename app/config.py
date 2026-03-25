from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_USER: str
    MONGO_PASS: str
    MONGO_HOST: str = "mongodb"
    MONGO_PORT: int = 27017
    MONGO_DB: str = "pagamentos_db"
    USERS_API_BASE: str = "http://18.228.48.67"

    @property
    def mongo_uri(self) -> str:
        return (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}"
            f"@{self.MONGO_HOST}:{self.MONGO_PORT}"
        )

    class Config:
        env_file = ".env"


settings = Settings()

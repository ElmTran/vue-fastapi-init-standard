from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Backend Starter"
    app_version: str = "0.1.0"
    debug: bool = True
    docs_enabled: bool = True
    environment: str = "dev"

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.dev"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
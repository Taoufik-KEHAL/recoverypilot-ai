from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the RecoveryPilot API."""

    environment: str = "local"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="RECOVERYPILOT_",
        extra="ignore",
    )


settings = Settings()

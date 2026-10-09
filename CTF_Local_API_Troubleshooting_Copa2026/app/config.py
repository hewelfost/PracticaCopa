from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    lab_api_key: str = "copa2026-lab"
    database_path: str = "data/copa_ctf.db"
    allowed_origins: str = "http://localhost:9999"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def origins(self) -> list[str]:
        return [item.strip() for item in self.allowed_origins.split(",") if item.strip()]

settings = Settings()

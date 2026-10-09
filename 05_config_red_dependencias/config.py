from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_port: int = 5433
    db_name: str = "postgres"
    db_user: str
    db_password: str
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Support API"
    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()

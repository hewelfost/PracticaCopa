from sqlalchemy import create_engine, text
from config import settings

url = f"postgresql+psycopg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
engine = create_engine(url, pool_pre_ping=True)

def check_database():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True

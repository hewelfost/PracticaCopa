from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, text
from config import settings

app = FastAPI(title="Dependency Challenge")

url = f"postgresql+psycopg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
engine = create_engine(url, pool_pre_ping=True, connect_args={"connect_timeout": 4})

@app.get("/health/live")
def live():
    return {"status": "alive"}

@app.get("/health/ready")
def ready():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"app": "healthy", "database": "healthy"}
    except Exception:
        return JSONResponse(status_code=503, content={"app": "healthy", "database": "unhealthy"})

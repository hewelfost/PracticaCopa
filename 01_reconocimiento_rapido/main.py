from fastapi import FastAPI, HTTPException
from config import settings
from database import check_database

api = FastAPI(title=settings.app_name)

@api.get("/")
def root():
    return {"service": settings.app_name, "status": "running"}

@api.get("/health/live")
def live():
    return {"status": "alive"}

@api.get("/health/ready")
def ready():
    try:
        check_database()
        return {"app": "healthy", "database": "healthy"}
    except Exception:
        raise HTTPException(status_code=503, detail="dependency unavailable")

@api.get("/api/version")
def version():
    return {"version": "1.0.0"}

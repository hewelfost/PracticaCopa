from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database import ping_database

router = APIRouter(tags=["health"])

@router.get("/health/live")
def live():
    return {"status": "alive"}

@router.get("/health/ready")
def ready():
    try:
        ping_database()
        return {"app": "healthy", "database": "healthy"}
    except Exception:
        return JSONResponse(
            status_code=503,
            content={"app": "healthy", "database": "unhealthy"},
        )

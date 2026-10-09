from fastapi import APIRouter, Header, HTTPException
from app.config import settings
from app.schemas import EchoRequest

router = APIRouter(prefix="/api/private", tags=["private"])

@router.get("/summary")
def private_summary(authorization: str | None = Header(default=None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="credentials required")

    if authorization != settings.lab_api_key:
        raise HTTPException(status_code=401, detail="invalid credentials")

    return {
        "service": "private-summary",
        "status": "authorized",
        "incidents_total": 0,
    }

@router.post("/echo")
def echo(payload: EchoRequest):
    return {"message": payload.message}

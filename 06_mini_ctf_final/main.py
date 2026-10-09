import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from config import settings

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("mini_ctf")

app = FastAPI(title="Mini CTF Incident API")

url = f"postgresql+psycopg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
engine = create_engine(url, pool_pre_ping=True, connect_args={"connect_timeout": 5})

class Incident(BaseModel):
    title: str
    severity: str = "medium"

incidents = {1: {"id": 1, "title": "API latency", "severity": "high"}}

@app.get("/health/live")
def live():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "alive"}
    except Exception:
        return JSONResponse(status_code=503, content={"status": "down"})

@app.get("/health/ready")
def ready():
    return {"app": "healthy", "database": "healthy"}

@app.post("/api/incidents")
def create_incident(payload: Incident):
    new_id = max(incidents.keys(), default=0) + 1
    item = {"id": new_id, **payload.model_dump()}
    incidents[new_id] = item
    return item

@app.get("/api/incidents")
def list_incidents():
    return list(incidents.values())

@app.get("/api/incidents/{incident_id}")
def get_incident(incident_id: int):
    item = incidents.get(incident_id)
    if item is None:
        return {"error": "not found"}
    if incident_id == 99:
        raise RuntimeError("simulated processing error")
    return item

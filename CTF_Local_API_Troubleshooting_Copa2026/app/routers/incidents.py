from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Incident
from app.schemas import IncidentCreate, IncidentUpdate

router = APIRouter(prefix="/api/incidents", tags=["incidents"])

@router.post("")
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    item = Incident(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "priority": item.priority,
    }

@router.get("")
def list_incidents(db: Session = Depends(get_db)):
    items = db.query(Incident).all()
    return [
        {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "priority": item.priority,
        }
        for item in items
    ]

@router.get("/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    item = db.get(Incident, incident_id)
    if item is None:
        return None
    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "priority": item.priority,
    }

@router.patch("/{incident_id}")
def update_incident(
    incident_id: int,
    payload: IncidentUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(Incident, incident_id)
    if item is None:
        return {"error": "incident not found"}

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "priority": item.priority,
    }

@router.delete("/{incident_id}")
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    item = db.get(Incident, incident_id)
    if item is None:
        return {"error": "incident not found"}

    db.delete(item)
    db.commit()
    return {"deleted": True}

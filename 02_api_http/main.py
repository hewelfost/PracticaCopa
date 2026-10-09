from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Ticket API")

class TicketCreate(BaseModel):
    title: str
    priority: str = "medium"

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    priority: Optional[str] = None

tickets = {
    1: {"id": 1, "title": "VPN unavailable", "priority": "high"},
    2: {"id": 2, "title": "Printer offline", "priority": "low"},
}

@app.get("/health/live")
def health():
    return {"status": "alive"}

@app.post("/api/tickets")
def create_ticket(payload: TicketCreate):
    new_id = max(tickets.keys(), default=0) + 1
    ticket = {"id": new_id, **payload.model_dump()}
    tickets[new_id] = ticket
    return ticket

@app.get("/api/tickets")
def list_tickets():
    return list(tickets.values())

@app.get("/api/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    return tickets.get(ticket_id)

@app.patch("/api/tickets/{ticket_id}")
def update_ticket(ticket_id: int, payload: TicketUpdate):
    current = tickets.get(ticket_id)
    if current is None:
        return {"error": "ticket not found"}
    current.update(payload.model_dump(exclude_unset=True))
    return current

@app.delete("/api/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    removed = tickets.pop(ticket_id, None)
    return {"deleted": bool(removed)}

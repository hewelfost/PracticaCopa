from fastapi import FastAPI, HTTPException, status
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

@app.get("/health/live", status_code=status.HTTP_200_OK)
def health():
    return {"status": "alive"}

@app.post("/api/tickets", status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate):
    new_id = max(tickets.keys(), default=0) + 1
    ticket = {"id": new_id, **payload.model_dump()}
    tickets[new_id] = ticket
    return ticket

@app.get("/api/tickets", status_code=status.HTTP_200_OK)
def list_tickets():
    return list(tickets.values())

@app.get("/api/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    ticket = tickets.get(ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket

@app.patch("/api/tickets/{ticket_id}")
def update_ticket(ticket_id: int, payload: TicketUpdate):
    current = tickets.get(ticket_id)
    if not current:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    
    update_data = payload.model_dump(exclude_unset=True)
    current.update(update_data)
    return current

@app.delete("/api/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: int):
    if ticket_id not in tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    tickets.pop(ticket_id)
    return None

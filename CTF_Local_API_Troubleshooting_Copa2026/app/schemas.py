from pydantic import BaseModel, Field
from typing import Optional

class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    description: str = Field(min_length=3, max_length=500)
    priority: str = "medium"

class IncidentUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=150)
    description: Optional[str] = Field(default=None, min_length=3, max_length=500)
    priority: Optional[str] = None

class EchoRequest(BaseModel):
    message: str = Field(min_length=1)

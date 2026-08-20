from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateTicket(BaseModel):
    title: str
    description : str
    status : str
class UpdateTicket(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class ticketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    class config:
        orm_mode = True



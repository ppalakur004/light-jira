from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(models.Ticket).all()
    return tickets

@app.post("/tickets", response_model=schemas.ticketResponse)
def create_ticket(ticket:schemas.CreateTicket,db: Session = Depends(get_db)):
    new_ticket = models.Ticket(title=ticket.title,description=ticket.description,status=ticket.status)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.put("/tickets/{ticket_id}", response_model=schemas.ticketResponse)
def update_ticket(ticket_id:int,ticket:schemas.UpdateTicket,db:session Session = Depends(get_db)):
    ticket_query = db.query(models.Ticket).filter(models.Ticket.id == ticket_id)
    updated_ticket = ticket_query.first()
    if not updated_ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    updated_ticket.title = ticket.title
    updated_ticket.description = ticket.description
    updated_ticket.status = ticket.status
    db.commit()
    db.refresh(updated_ticket)
    return updated_ticket

@app.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id:int,db:Session = Depends(get_db)):
    ticket_query = db.query(models.Ticket).filter(models.Ticket.id == ticket_id)
    deleted_ticket = ticket_query.first()
    if not deleted_ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    ticket_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
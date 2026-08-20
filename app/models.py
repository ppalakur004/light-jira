from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Ticket(Base)
    __tablename__ = "tickets"
    id = Column(Integer,primary_key=True,index=True)
    title = column(String,index=True)
    description = Column(String,index=True)
    status = Column(String,index=True)
    created_at = Column(DateTime,index=True)
    updated_at = Column(DateTime,index=True)


    
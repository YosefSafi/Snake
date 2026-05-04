from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String)
    link = Column(String, unique=True, nullable=False)
    source = Column(String)
    description = Column(Text)
    salary = Column(String)
    match_score = Column(Float)
    status = Column(String, default="Not Applied")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_checked = Column(DateTime, default=datetime.utcnow)

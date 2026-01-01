from sqlalchemy import Column, Integer, String, Date, Text, DateTime
from .database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String, index=True)
    company = Column(String, index=True)
    location = Column(String, index=True)

    employment_type = Column(String, index=True)
    source = Column(String, index=True)

    min_salary = Column(Integer, nullable=True)
    max_salary = Column(Integer, nullable=True)
    currency = Column(String, nullable=True)

    posted_date = Column(Date, nullable=True)
    job_url = Column(String)

    description = Column(Text)

    scraped_at = Column(DateTime, default=datetime.utcnow)

import logging
from typing import List, Dict
from jobforge.db.session import SessionLocal
from jobforge.db.models import Job
from sqlalchemy.exc import IntegrityError
from datetime import datetime

logger = logging.getLogger(__name__)

class JobSearchEngine:
    def __init__(self):
        self.db = SessionLocal()

    def add_job(self, job_data: Dict):
        """Adds a job to the database."""
        job = Job(
            title=job_data["title"],
            company=job_data["company"],
            location=job_data.get("location"),
            link=job_data["link"],
            source=job_data.get("source"),
            description=job_data.get("description"),
            last_checked=datetime.utcnow()
        )
        self.db.add(job)
        try:
            self.db.commit()
            logger.info(f"Added job: {job.title} at {job.company}")
        except IntegrityError:
            self.db.rollback()
            logger.debug(f"Job already exists: {job.link}")

    def list_jobs(self):
        return self.db.query(Job).all()

import logging
from typing import List, Dict
from jobforge.db.session import SessionLocal
from jobforge.db.models import Job
from sqlalchemy.exc import IntegrityError
from datetime import datetime, UTC

logger = logging.getLogger(__name__)

class JobSearchEngine:
    def __init__(self, db_session=None):
        self.db = db_session or SessionLocal()

    def add_job(self, job_data: Dict):
        """Adds a job to the database."""
        job = Job(
            title=job_data["title"],
            company=job_data["company"],
            location=job_data.get("location"),
            link=job_data["link"],
            source=job_data.get("source"),
            description=job_data.get("description"),
            last_checked=datetime.now(UTC)
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

    def get_job(self, job_id: int):
        return self.db.query(Job).filter(Job.id == job_id).first()

    def update_job_status(self, job_id: int, status: str):
        job = self.get_job(job_id)
        if job:
            job.status = status
            self.db.commit()
            return True
        return False

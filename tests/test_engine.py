import pytest
from jobforge.search.engine import JobSearchEngine
from jobforge.db.session import init_db, get_engine, get_session_factory
from jobforge.db.models import Base
import os
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def test_db():
    engine = get_engine()
    # Ensure we are using a test db if not already set
    if "test" not in str(engine.url):
        pytest.skip("Not a test database")
    
    Base.metadata.create_all(bind=engine)
    Session = get_session_factory(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_add_and_list_job(test_db):
    engine = JobSearchEngine(db_session=test_db)
    job_data = {
        "title": "Test Engineer",
        "company": "Test Org",
        "link": "https://test.com/1",
        "location": "Remote"
    }
    engine.add_job(job_data)
    jobs = engine.list_jobs()
    assert len(jobs) == 1
    assert jobs[0].title == "Test Engineer"

def test_duplicate_job(test_db):
    engine = JobSearchEngine(db_session=test_db)
    job_data = {
        "title": "Test Engineer",
        "company": "Test Org",
        "link": "https://test.com/1"
    }
    engine.add_job(job_data)
    engine.add_job(job_data)
    jobs = engine.list_jobs()
    assert len(jobs) == 1

def test_update_status(test_db):
    engine = JobSearchEngine(db_session=test_db)
    engine.add_job({"title": "Test", "company": "Co", "link": "https://test.com/2"})
    job = engine.list_jobs()[0]
    engine.update_job_status(job.id, "Applied")
    updated_job = engine.get_job(job.id)
    assert updated_job.status == "Applied"

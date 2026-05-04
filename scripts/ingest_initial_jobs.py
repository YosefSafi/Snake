import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from jobforge.search.engine import JobSearchEngine
from jobforge.db.session import init_db

def ingest():
    init_db()
    engine = JobSearchEngine()
    
    jobs = [
        {"title": "React/React Native Developer", "company": "Wint", "location": "Gothenburg", "link": "https://wint.se/jobs/1", "source": "Indeed"},
        {"title": ".NET Systemutvecklare", "company": "Nexer AB", "location": "Gothenburg", "link": "https://nexergroup.com/jobs/2", "source": "Ledigajobb.se"},
        {"title": "Frontend Engineer", "company": "Consilium Safety Group", "location": "Gothenburg", "link": "https://consilium.se/jobs/3", "source": "Jooble"},
        {"title": "Webbutvecklare", "company": "Göteborgs Stad", "location": "Gothenburg", "link": "https://goteborg.se/jobs/4", "source": "Platsbanken"},
        {"title": "IT-support Servicedesk", "company": "Peoplez", "location": "Gothenburg", "link": "https://peoplez.se/jobs/5", "source": "Indeed"},
        {"title": "IT Support Lead", "company": "InfraCom", "location": "Gothenburg", "link": "https://infracom.se/jobs/6", "source": "LinkedIn"},
    ]
    
    for job in jobs:
        engine.add_job(job)
    
    print(f"Successfully ingested {len(jobs)} jobs.")

if __name__ == "__main__":
    ingest()

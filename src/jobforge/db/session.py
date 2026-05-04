from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jobforge.core.config import settings
from jobforge.db.models import Base

def get_engine():
    return create_engine(settings.DATABASE_URL)

def get_session_factory(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(engine=None):
    if engine is None:
        engine = get_engine()
    Base.metadata.create_all(bind=engine)

# Default session for the app
engine = get_engine()
SessionLocal = get_session_factory(engine)

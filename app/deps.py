from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import Base

DATABASE_URL = "postgresql://user:password@db:5432/memes_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_database():
    Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from models import Base




DATABASE_URL = "postgresql://username:password@rds.amazonaws.com:5432/database_name"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER: str = "postgres"
POSTGRES_PASSWORD: str = "lilit"
POSTGRES_SERVER: str = "localhost"
POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
POSTGRES_DB: str = "jobboard"
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

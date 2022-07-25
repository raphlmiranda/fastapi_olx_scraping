from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

SQLALCHEMY_DATABASE_URL = f"postgresql://{config('POSTGRES_USERNAME')}:{config('POSTGRES_PASSWORD')}@db:5432/{config('POSTGRES_DB')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

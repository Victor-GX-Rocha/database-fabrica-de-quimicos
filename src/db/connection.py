""" Manages the connection with the database. """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .models import DatabaseConnector 

DATABASE_URL: str = DatabaseConnector().url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def session_scope():
    """ Creates a temp session. """
    try:
        session  = SessionLocal()
        yield session
        session.commit()
    except Exception as e:
        print(f"Erro ao realizar comando SQL: {e}")
        session.rollback()


def create_tables() -> None:
    """ Creates all defined tables if it not exist. """
    Base.meatada.create_all(engine)

""" Manages the connection with the database. """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase
from contextlib import contextmanager

from .models import DatabaseConnector 

DATABASE_URL: str = DatabaseConnector().url
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

@contextmanager
def session_scope():
    """ 
    Creates a temporary session within a scope that can be accessed with a with statement.
    
    Automatically performs:
    - Opens the session.
    - Commits at the end of the operation.
    - Rollback in case of error.
    - Closes the temporary session.
    """
    try:
        session = SessionLocal()
        yield session
        session.commit()
    except Exception as e:
        print("Erro de sessão:", e)
        session.rollback()
    finally:
        session.close()


def create_tables() -> None:
    """ Creates all defined tables if it not exist. """
    Base.metadata.create_all(engine)

create_tables()

__all__ = [
    "Base",
    "session_scope",
    "create_tables",
]

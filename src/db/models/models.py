""" Models for database tools. """

import os
from dotenv import load_dotenv
from dataclasses import dataclass, field

load_dotenv()

@dataclass
class DatabaseConnector:
    """
    Stores the data to construct the database URL Connection.
    Args:
        database_model (str): Defines the SQL model. (PostgreSQL, MySQL, SQLite...)
        library (str): Python library dependence. (psycopg2, mysqlclient, sqlite3...)
        user (str): SQL user.
        password (str): Passowrd to database.
        host (str): Host connection code.
        port (int): Port number.
        database (str): Database name.
        url (str): The URL database connection.
    """
    database_model: str = os.getenv("DATABASE_MODEL")
    library: str = os.getenv("LIBRARY")
    user: str = os.getenv("USER")
    password: str = os.getenv("PASSWORD")
    host: str = os.getenv("HOST")
    port: int = os.getenv("PORT", 5432)
    database: str = os.getenv("DATABASE")
    url: str = field(init=False)  # Campo não incluído no __init__
    
    def __post_init__(self) -> str:
        """ Construct the database url after init the dataclass attributes. """
        self.url = f"{self.database_model}+{self.library}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


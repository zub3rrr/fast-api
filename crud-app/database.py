"""
This module sets up the database connection and ORM base class using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
declarative_base(): Creates a base class for declarative models in SQLAlchemy. 
All your ORM models/classes will inherit from this base class to be mapped to database tables.
Means Pyhton classes can be defined that correspond to database tables.

sessionmaker(): A factory function that creates new SQLAlchemy Session objects.
Sessions manage database transactions and act as your interface for database operations.
"""

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

"""
connect_args={"check_same_thread": False} : This argument is specific to SQLite.
It allows the SQLite database to be accessed from different threads.
By default, SQLite restricts database connections to the thread that created them.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

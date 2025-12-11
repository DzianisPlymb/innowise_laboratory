from sqlalchemy import Column, Integer, String
from .dbconnect import Base

# Define the Book model which maps to the "books" table in the database
class Book(Base):
    __tablename__ = "books" # name of the table in database

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)

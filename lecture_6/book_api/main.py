from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .dbconnect import Base, engine, SessionLocal
from . import models

from . import schemas


app = FastAPI()

# создаём таблицу книг
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "deleted"}


@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author
    if book.year is not None:
        db_book.year = book.year

@app.get("/books/search/", response_model=list[schemas.Book])
def search_books(
    q: Optional[str] = Query(None, description="Search in title or author"),
    year: Optional[int] = Query(None, description="Filter by year"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Book)

    if q:
        pattern = f"%{q}%"
        query = query.filter(
            models.Book.title.ilike(pattern) |
            models.Book.author.ilike(pattern)
        )

    if year is not None:
        query = query.filter(models.Book.year == year)

    return query.all()

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate, Book
from app.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/books", response_model=Book)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new book entry."""
    new_book = Book(**book.dict(), user_id=current_user.id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/books", response_model=List[Book])
def read_books(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all books for the current user."""
    return db.query(Book).filter(Book.user_id == current_user.id).all()


@router.get("/books/{book_id}", response_model=Book)
def read_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get a single book by ID."""
    book = db.query(Book).filter(Book.id == book_id, Book.user_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update a book's details."""
    book = db.query(Book).filter(Book.id == book_id, Book.user_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for field, value in book_update.dict(exclude_unset=True).items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


@router.delete("/books/{book_id}", response_model=dict)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a book."""
    book = db.query(Book).filter(Book.id == book_id, Book.user_id == current_user.id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

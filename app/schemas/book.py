from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    isbn: Optional[str] = None
    publication_date: Optional[date] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None


class BookInDB(BookBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Book(BookInDB):
    pass

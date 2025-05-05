from sqlalchemy.orm import Session

from app.models.base import Base
from app.db.database import engine
from app.models import User, Book


def init_db() -> None:
    # Create tables
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
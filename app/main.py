from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.init_db import init_db
from app.api.v1.auth import router as auth_router
from app.api.v1.book import router as book_router

app = FastAPI(
    title="Book Management API",
    description="An API to manage books with user authentication",
    version="1.0.0",
)

# Allow all CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on startup
@app.on_event("startup")
def startup_db_client():
    init_db()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}

# Routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(book_router, prefix="/api", tags=["books"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

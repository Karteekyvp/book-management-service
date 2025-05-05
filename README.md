# 📚 Book Management API — Built with FastAPI, PostgreSQL, Docker

Welcome to your **complete Book Management Microservice** — built from scratch using FastAPI, SQLAlchemy, PostgreSQL, JWT authentication, Pytest, and Docker.

This README walks you through:
- ✅ What this project does
- 🧱 How it's designed
- 🛠️ How to set it up
- 🔐 How to use secure APIs
- 🧪 How to test it
- 🐳 How to Dockerize it
- 🚀 How to prepare for CI/CD & cloud deployment

---

## 📖 What Does This App Do?

Think of it like a **digital bookshelf** you can:
- 🔑 Log in to securely
- ➕ Add books
- 📚 View your collection
- 🔍 Search by title, author, or genre
- ✏️ Edit book info
- ❌ Delete books

Everything is stored in a **PostgreSQL database**, and every action goes through a clean, fast **REST API**.

---

## 🧱 Architecture Overview

| Layer         | Description                                       |
|---------------|---------------------------------------------------|
| API Layer     | FastAPI endpoints (clean, async, auto-documented) |
| Auth Layer    | Secure user login with JWT                        |
| Data Layer    | SQLAlchemy models and DB access                   |
| DB            | PostgreSQL (runs in Docker)                       |
| Security      | OAuth2 + JWT tokens                               |
| Testing       | Pytest (unit) + Behave (BDD)                      |
| DevOps Ready  | Docker + env vars + GitHub Actions ready          |

---

## 🔧 Setup Guide — Step-by-Step

### 🔹 1. Clone the Project
```bash
git clone https://github.com/yeluru/book_management_service.git
cd book_management_service
```

### 🔹 2. Create Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
```

### 🔹 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 🔹 4. Start PostgreSQL with Docker
```bash
docker-compose up -d
```

> This starts a PostgreSQL container at `localhost:5432` with:
> - user: `postgres`
> - password: `postgres`
> - db: `book_management`

---

## ⚙️ Run the App

### ✅ Run FastAPI Server
```bash
python -m app.main
```

- Visit: `http://localhost:8000`
- Docs: `http://localhost:8000/docs` (Swagger UI)

---

## 🔐 Auth Flow

| Action         | API Endpoint                |
|----------------|-----------------------------|
| Register       | `POST /api/v1/auth/register` |
| Login          | `POST /api/v1/auth/login`    |
| Protected APIs | Use `Authorization: Bearer <token>` header |

You must **log in first** to receive a token. Use that token to:
- Add/update/delete books
- Access private endpoints

---

## 📘 Book Endpoints

| Operation     | Method & Path              | Auth Required |
|---------------|----------------------------|---------------|
| Add Book      | POST `/api/v1/books`       | ✅ Yes         |
| Get All Books | GET `/api/v1/books`        | ✅ Yes         |
| Get One Book  | GET `/api/v1/books/{id}` | ✅ Yes         |
| Update Book   | PUT `/api/v1/books/{id}` | ✅ Yes         |
| Delete Book   | DELETE `/api/v1/books/{id}` | ✅ Yes       |

---

## 🧪 Testing

### ▶️ Run Unit Tests
```bash
pytest
```

### 🧬 Run BDD Tests
```bash
behave
```

---

## 🐳 Docker-Ready Setup

> You already have a working `docker-compose.yml` for PostgreSQL.

To run API inside a container (recommended in production):
- Add `Dockerfile` (to be included soon)
- Build + run FastAPI app

---

## 📂 Project Structure

```
book_management_service/
├── app/
│   ├── api/v1/       # All API endpoints (auth, book)
│   ├── auth/         # JWT creation and verification
│   ├── db/           # Database setup and connection
│   ├── models/       # SQLAlchemy DB models
│   ├── schemas/      # Request & response validation
│   ├── config.py     # App configuration
│   └── main.py       # App entry point
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 💡 Explained Like You're 10

- **API**: A magic window — you make a request, and it gives you what you want.
- **JWT**: A VIP wristband you wear — once you're in, you can go anywhere.
- **Docker**: A lunchbox that packs your project so it works anywhere.
- **Database**: A smart notebook that never forgets.

---

## 🚀 CI/CD & Deployment

### 💡 Future Enhancements:
- Add `Dockerfile` and deploy full stack with Docker Compose
- Add GitHub Actions for test → build → deploy
- Deploy backend on EC2, Lambda, or ECS
- Add search query param: `/api/v1/books/search?q=python`
- Add cover images & book reviews

---

## 👨‍💻 Author

Built with 💛 by Ravi  
_“For learners, by learners.”_

---

_Last updated: 2025-05-05_

---

## 🗂️ File-by-File Explanation (What Does Each File Do?)

### 📁 `app/`

#### `main.py`
The entry point of the app. It creates the FastAPI application, connects all the routers (auth + books), adds CORS (security headers), and runs database setup on startup.

#### `config.py`
Stores environment variables (like database URLs or token expiration times). Think of this as the app’s settings file.

---

### 📁 `auth/`

#### `__init__.py`
Shortcut to expose key functions from `jwt.py`, so other parts of the app can easily import `get_current_user` and token tools.

#### `jwt.py`
Handles all authentication:
- Hashes passwords using bcrypt
- Verifies login passwords
- Generates secure tokens (JWTs)
- Extracts users from those tokens

This is the **digital security system** of the app.

---

### 📁 `db/`

#### `database.py`
Sets up the connection to PostgreSQL using SQLAlchemy. Defines the base class for models and provides a function to open/close DB sessions.

#### `init_db.py`
Creates all database tables when the app starts up. Think of this as your database “setup crew”.

---

### 📁 `models/`

#### `user.py`
Defines what a user looks like in the database (id, email, password, created_at). It also links users to their books.

#### `book.py`
Defines what a book looks like (title, author, genre, etc.). Each book is linked to a user using a foreign key.

#### `base.py`
A shared base class for all models. Sets automatic timestamps and handles table naming.

---

### 📁 `schemas/`

#### `user.py`
Defines data formats for:
- Registering a user
- Logging in
- Returning user info
- Generating JWT token payloads

Uses Pydantic to validate everything.

#### `book.py`
Defines what book data should look like when:
- Creating a book
- Updating a book
- Returning a book (as response)

This ensures the data stays clean and consistent.

---

### 📁 `api/v1/`

#### `__init__.py`
Organizes all version 1 endpoints under one router (`api_router`). Adds both auth and book routers.

#### `auth.py`
Contains `/register` and `/login` routes:
- Verifies user existence
- Hashes passwords
- Returns JWT token on successful login

#### `book.py`
Contains:
- `POST /books` → Add a book
- `GET /books` → List all books
- `GET /books/{id}` → Get one
- `PUT /books/{id}` → Edit a book
- `DELETE /books/{id}` → Remove it

Every route requires the user to be logged in with a valid token.

---

### 🐳 `docker-compose.yml`
Sets up and runs PostgreSQL in a container with default credentials.

---

### 📄 `requirements.txt`
Lists all required Python libraries to make the app work.

---

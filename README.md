# 📚 Book Management API (Built with FastAPI & PostgreSQL)

Welcome! This project is a **Book Management API** — a small web service that lets you do things like:
- Register and log in
- Add your favorite books
- Search and update them
- Delete them when you're done

It works kind of like a tiny online library!

---

## 🧠 What’s This All About?

Think of it like a **digital notebook for books**, where you can:
- Tell it the name, author, and genre of a book.
- Ask it to list all your books.
- Change book details if you made a mistake.
- Remove books you don’t want anymore.
- Keep it all secure with login and password.

And guess what? You talk to it not with buttons or screens — but with **URLs called APIs**. Like magic instructions!

---

## 🛠️ What Did We Use to Build It?

| Tool | Purpose |
|------|---------|
| **FastAPI** | It’s the brain — it understands requests and gives replies. |
| **PostgreSQL** | The memory — it stores your books and users. |
| **SQLAlchemy** | The translator — helps FastAPI talk to the database. |
| **JWT** | The security guard — keeps your book shelf safe. |
| **Docker** | The moving truck — it packs everything neatly so it can run anywhere. |

---

## 🧾 Features

- 📘 **CRUD for books** (Create, Read, Update, Delete)
- 🔐 **Authentication** with username & password
- 🔎 **Search by title, author, or genre**
- 💬 **Well-documented** with Swagger UI at `/docs`
- 🐳 **Runs in Docker**
- 🧪 **Tested** with Pytest & Behave

---

## 🖼️ How It Works (Use Case)

### Imagine Ravi logs in:
1. 🔑 Registers an account (like creating a profile).
2. 🪪 Logs in with a password.
3. 📗 Adds books like *Harry Potter* or *The Hobbit*.
4. 🔍 Searches for all fantasy books.
5. ✏️ Edits the title if there's a typo.
6. ❌ Deletes books he doesn’t want anymore.

---

## ⚙️ Project Structure

```
book_management_service/
├── app/
│   ├── api/          # Routes (URLs)
│   ├── auth/         # Login, tokens, password hashing
│   ├── db/           # Database connection and setup
│   ├── models/       # What a "Book" or "User" looks like
│   ├── schemas/      # Input/output shapes
│   ├── config.py     # Environment settings
│   └── main.py       # App entry point
├── docker-compose.yml  # Runs PostgreSQL DB
├── requirements.txt     # Python libraries needed
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/your-repo/book_management_service.git
cd book_management_service
```

### 2. Create a Python environment

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
```

### 3. Install all required libraries

```bash
pip install -r requirements.txt
```

### 4. Start PostgreSQL with Docker

```bash
docker-compose up -d
```

This spins up a PostgreSQL database container. Think of it like turning on a refrigerator where we’ll store your books and users.

### 5. Run the API locally

```bash
python -m app.main
```

Go to your browser and open:
- 🌐 `http://localhost:8000` → You’ll see a welcome message!
- 📚 `http://localhost:8000/docs` → Interactive API documentation

---

## 🔐 Authentication

To use protected routes (like adding or editing books), you must:

1. **Register** via `POST /api/auth/register`
2. **Login** via `POST /api/auth/login`
   - It returns a **JWT token**.
3. Include the token in the **Authorization header**:
   ```
   Authorization: Bearer <your_token_here>
   ```

---

## 🧪 Testing

To run tests:

```bash
pytest
```

For behavior-driven tests (written like stories):

```bash
behave
```

---

## 📦 Docker Setup

To run the app fully in Docker (optional):

> _(Steps will be included once a Dockerfile is present)_

---

## 🧠 Concepts Explained Like You’re 10

- **API**: Like a menu at a restaurant. You tell it what you want (a book!), and it gives it to you.
- **JWT**: Like a secret pass. Once you log in, you get a special key. Show it next time so the system knows it’s you.
- **Docker**: Like a lunchbox for software — pack it once, carry it anywhere.
- **Database**: A smart notebook that remembers every book you added.

---

## 📌 Future Improvements

- Add unit and integration test coverage
- Deploy to AWS with CI/CD
- Add user profile settings
- Implement book ratings & reviews

---

## 🧑‍💻 Author

Built by Ravi and team — for learners, by learners.

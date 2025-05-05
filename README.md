# 📚 Book Management API (Built with FastAPI & PostgreSQL)

Welcome! This project is a **Book Management API** — a small web service that lets you:
- Register and log in securely
- Add your favorite books
- Search them by title, author, or genre
- Edit or delete them when needed

It works kind of like your own little online library.

---

## 🧠 What’s This All About?

Imagine you're keeping track of your favorite books — their titles, authors, genres, ISBN numbers — all in a digital app. But instead of a big, clunky website, this app talks in a language that other apps understand: **APIs**.

You can:
- 📥 Add books you love
- 📖 List all the books in your collection
- 🕵️‍♀️ Search books by keywords
- ✏️ Edit their details
- ❌ Delete them
- 🔒 Keep everything secure by requiring login

Even better — this API could be plugged into a website, mobile app, or even used by another team at work.

---

## 🛠️ What Technologies Were Used?

| Tool | Purpose |
|------|---------|
| **FastAPI** | The brain – handles all the user instructions (API calls). |
| **PostgreSQL** | The memory – stores all your books and users. |
| **SQLAlchemy** | The translator – connects FastAPI to the database. |
| **JWT** | The security pass – lets users access their data safely. |
| **Docker** | The lunchbox – packages the whole thing to run anywhere easily. |
| **Pytest + Behave** | Testing tools – to make sure everything works as expected. |

---

## 🧾 Features

- ✅ Secure user registration and login
- 📘 CRUD for books (Create, Read, Update, Delete)
- 🔍 Search by title, author, or genre
- 🔐 JWT-based authentication for protected routes
- 📚 Auto-generated API documentation with Swagger UI at `/docs`
- 🐳 Docker support for consistent environments
- 🧪 Testing with unit tests (`pytest`) and behavior-driven tests (`behave`)

---

## 🖼️ How It Works – A Day in the Life of the API

### Imagine Ravi logs in:
1. 🔑 He registers an account.
2. 🪪 He logs in using his credentials.
3. 📗 He adds a few books like *The Alchemist* and *To Kill a Mockingbird*.
4. 🔍 He searches for all books by author "Paulo Coelho".
5. ✏️ He fixes a typo in one of the book titles.
6. ❌ He deletes a book he’s no longer interested in.

Each of these steps is handled by a specific **API endpoint**. The system is smart, fast, and secure.

---

## ⚙️ Project Folder Structure

```
book_management_service/
├── app/
│   ├── api/          # API route definitions (URLs)
│   ├── auth/         # JWT token creation, password hashing, current user
│   ├── db/           # Database connection and setup scripts
│   ├── models/       # SQLAlchemy models for Book and User
│   ├── schemas/      # Pydantic models for request and response formats
│   ├── config.py     # Environment variables and settings loader
│   └── main.py       # Main app bootstrapper
├── docker-compose.yml  # PostgreSQL setup using Docker
├── requirements.txt     # Required Python libraries
└── README.md
```

---

## 🚀 Getting Started (Step-by-Step)

### 1. Clone the Project
```bash
git clone https://github.com/yeluru/book_management_service.git
cd book_management_service
```

### 2. Set Up a Python Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. Start the PostgreSQL Database Using Docker
```bash
docker-compose up -d
```

This spins up a PostgreSQL container in the background. Think of it as turning on a smart notebook to save all your data.

### 5. Run the API
```bash
python -m app.main
```

Open in your browser:
- `http://localhost:8000` → Welcome message
- `http://localhost:8000/docs` → Swagger UI to explore and test APIs interactively

---

## 🔐 Authentication Overview

All book operations (add/edit/delete) require authentication.

1. Register: `POST /api/auth/register`
2. Login: `POST /api/auth/login`  
   (returns a JWT token)

3. Use the token in future requests:
```
Authorization: Bearer <your_token>
```

---

## 🧪 Running Tests

### Unit Tests (code-level testing)
```bash
pytest
```

### BDD Tests (user behavior stories)
```bash
behave
```

These ensure the system behaves the way real users expect — like confirming login works or book creation is successful.

---

## 📦 Docker-Friendly (Future)

You already have Docker Compose for the database. You can add a `Dockerfile` to run the API server inside a container. This is great for:
- Team collaboration
- Cloud deployment
- Avoiding “works on my machine” issues

---

## 👶 Concepts Explained Simply

- **API**: Like placing an order at a restaurant. You don’t cook — you just say what you want.
- **JWT**: A magic pass. Once you log in, you get a token. Flash it for every request.
- **Docker**: A backpack with your whole project inside. Grab it and go — it works everywhere.
- **Database**: Like a bookshelf. It remembers every book you've added.

---

## 📌 Future Plans

- Add automated tests for all endpoints
- Add a Dockerfile and full Docker setup
- Deploy to AWS using GitHub Actions or Jenkins
- Add book ratings, cover images, and user profiles
- Support multiple languages and search filters

---

## 🧑‍💻 Built With 💛 by Ravi

This project was built as a real-world, end-to-end example of how to design, secure, test, and deploy a FastAPI microservice for managing books. Whether you’re a developer, student, or just curious — it’s made to be easy to understand and extend.

Explore it, break it, build on it!


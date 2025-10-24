# 🧩 CRUD App (FastAPI + SQLAlchemy)

A simple FastAPI CRUD (Create, Read, Update, Delete) application demonstrating modular architecture using Pydantic, SQLAlchemy, and Uvicorn.
This project provides an Employee management API that handles employee creation, updates, and retrieval using proper schema validation.
## 🚀 Project Structure
```
crud-app/
│
├── schemas.py          # Pydantic models for request & response validation
├── models.py          # SQLAlchemy ORM models
├── crud.py           # CRUD operation functions
├── database.py       # Database engine & session setup
├── main.py          # FastAPI app entry point
├── pyproject.toml   # Project metadata and dependencies
└── README.md        # Project documentation
```

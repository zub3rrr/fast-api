# 🧩 CRUD App (FastAPI + SQLAlchemy)

A simple FastAPI CRUD (Create, Read, Update, Delete) application demonstrating modular architecture using Pydantic, SQLAlchemy, and Uvicorn.
This project provides an Employee management API that handles employee creation, updates, and retrieval using proper schema validation.
## 🚀 Project Structure
```
crud-app/
│
├── schemas.py       # Pydantic models for request & response validation
├── models.py        # SQLAlchemy ORM models
├── crud.py          # CRUD operation functions
├── database.py      # Database engine & session setup
├── main.py          # FastAPI app entry point
├── pyproject.toml   # Project metadata and dependencies
└── README.md        # Project documentation
```

## Tech - Stack 
| Component           | Description                             |
| ------------------- | --------------------------------------- |
| **FastAPI**         | API framework                           |
| **SQLAlchemy**      | ORM for database interactions           |
| **Pydantic**        | Data validation and schema management   |
| **Uvicorn**         | ASGI server for running the FastAPI app |
| **Email Validator** | For validating employee email IDs       |


## Installation 
### 1. Clone the repository
```
pip install uv

git clone https://github.com/your-username/crud-app.git

cd crud-app
```
### 2. Simply run below command 
```
uv run uvicorn main:app --reload
```

### 🌐 Access API Documentation

Once the app is running, open:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

| Method   | Endpoint          | Description             |
| -------- | ----------------- | ----------------------- |
| `POST`   | `/employees/`     | Create a new employee   |
| `GET`    | `/employees/`     | Retrieve all employees  |
| `GET`    | `/employees/{id}` | Retrieve employee by ID |
| `PUT`    | `/employees/{id}` | Update employee details |
| `DELETE` | `/employees/{id}` | Delete employee record  |




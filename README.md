# Mini Task Manager API

A simple REST API built with FastAPI for creating, reading, updating, and deleting tasks.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- HTTPX

## Features

- Create tasks
- Get all tasks
- Get a task by ID
- Update tasks
- Delete tasks
- Input validation
- Error handling
- Automated API testing

## Project Structure

```text
Mini task manager API/
├── app/
│   ├── routers/
│   │   └── tasks.py
│   ├── database.py
│   ├── model.py
│   ├── schemas.py
│   └── main.py
├── tests/
│   └── test_tasks.py
├── .gitignore
├── requirements.txt
├── README.md
└── test.http
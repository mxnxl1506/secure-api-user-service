# Secure API User Service

## Overview
Secure API User Service is a FastAPI backend project designed to demonstrate secure API development, authentication, input validation, and database integration.

The project was built to showcase backend engineering skills aligned with modern full-stack and enterprise application requirements.

## Features
- User registration and login
- Password hashing using bcrypt
- JWT-based authentication
- Protected profile endpoint
- API key protected internal endpoint
- Input validation with Pydantic
- SQLite database integration with SQLAlchemy
- Auto-generated API documentation using FastAPI

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- Python-JOSE

## Key Skills Demonstrated
- Backend API development
- Authentication and authorization
- Secure coding practices
- Database integration
- Input validation and error handling
- RESTful service design

## Project Structure

```text
secure-api-user-service/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes.py
├── requirements.txt
├── README.md
└── .gitignore
```


## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```
### Start the server
```bash
uvicorn app.main:app --reload
```
### Open the API docs
```bash
http://127.0.0.1:8000/docs
```
## Notes
This project is intended to demonstrate secure backend engineering practices including authentication, protected routes, validation, and API design.

## Root Files
```bash
├── requirements.txt
├── README.md
└── .gitignore
```

# Enterprise HRMS Backend

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A scalable **Enterprise Human Resource Management System (HRMS) backend** built using **FastAPI, PostgreSQL, and SQLAlchemy**.
This project demonstrates modern backend development practices including **REST API design, relational database modeling, and schema validation**.

---

# Project Overview

The Enterprise HRMS Backend provides APIs for managing employees within organizations.
It allows organizations to store and manage employee data using a structured relational database.

The backend is built using **FastAPI**, which provides high performance and automatic API documentation through Swagger UI.

---

# Tech Stack

Backend Framework
FastAPI

Database
PostgreSQL (Supabase)

ORM
SQLAlchemy

Data Validation
Pydantic

Server
Uvicorn

Version Control
Git & GitHub

---

# System Architecture

The backend follows a layered architecture.

```
        Client / User
             │
             │ HTTP Requests
             ▼
        FastAPI Server
           (main.py)
             │
             ▼
      ┌────────────────┐
      │   CRUD Layer   │
      │   (crud.py)    │
      └────────────────┘
             │
             ▼
      ┌────────────────┐
      │ SQLAlchemy ORM │
      │ (models.py)    │
      └────────────────┘
             │
             ▼
        PostgreSQL
        (Supabase DB)
```

---

# Project Structure

```
enterprise_hrms
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Database Design

The system uses a relational database with the following structure.

Organizations Table

id (UUID)
name (string)
domain (string)
created_at (timestamp)

Employees Table

id (UUID)
organization_id (UUID, Foreign Key)
employee_code (string)
first_name (string)
last_name (string)
email (string)
hire_date (date)
employment_type (string)
phone (string)
status (string)
created_at (timestamp)
updated_at (timestamp)

Relationship

```
Organization (1)
      │
      │
      ▼
Employees (Many)
```

Each employee belongs to an organization.

---

# API Endpoints

Create Employee

POST /employees

Example Request

```
{
  "organization_id": "550e8400-e29b-41d4-a716-446655440000",
  "employee_code": "EMP001",
  "first_name": "Shivam",
  "last_name": "Kumar",
  "email": "shivam.kumar@example.com",
  "hire_date": "2026-02-27",
  "employment_type": "Full-time",
  "phone": "9876543210",
  "status": "Active"
}
```

---

Get Employees

GET /employees

Returns a list of all employees.

---

Delete Employee

DELETE /employees/{emp_id}

Deletes an employee by ID.

---

# API Request Flow

```
User Request
     │
     ▼
FastAPI Endpoint
(main.py)
     │
     ▼
Pydantic Validation
(schemas.py)
     │
     ▼
CRUD Operations
(crud.py)
     │
     ▼
SQLAlchemy ORM
(models.py)
     │
     ▼
PostgreSQL Database
(Supabase)
     │
     ▼
Response Returned to Client
```

---

# Running the Project Locally

Clone the repository

```
git clone https://github.com/shivam-9s/enterprise-hrms-backend.git
```

Navigate to project folder

```
cd enterprise-hrms-backend
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run the FastAPI server

```
uvicorn main:app --reload
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

These allow testing APIs directly from the browser.

---

# Key Features

Employee CRUD APIs
Organization to Employee relationship
PostgreSQL database integration
FastAPI automatic API documentation
Pydantic data validation
Clean modular backend architecture

---

# Future Improvements

Organization management APIs
Department management system
Employee attendance tracking
Payroll management module
JWT authentication system
Role based access control
Admin dashboard

---

# Author

Shivam Kumar

---

# License

This project is developed for educational and learning purposes.

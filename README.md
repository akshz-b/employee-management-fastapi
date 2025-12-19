# Employee Management System – FastAPI

This project is a backend service built using FastAPI that performs CRUD operations on a MySQL Server database for managing employees.

The application supports creating, retrieving, updating, soft-deleting, and listing employees with pagination. It follows a clean project structure and uses SQLAlchemy ORM for database interaction.

Technology stack used in this project:
Python 3.11
FastAPI
SQLAlchemy
MySQL Server
Uvicorn
Pydantic

Project folder structure:

employee_api/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ └── routes/
│ └── employees.py
├── .env
├── venv/
└── README.md

Database details:

Database name: employee_db
Table name: employees

Table structure:

id – INT, primary key, auto increment
name – VARCHAR(100)
email – VARCHAR(100), unique
department – VARCHAR(50)
salary – DECIMAL(10,2)
is_active – BOOLEAN
created_at – DATETIME

Prerequisites

- Python 3.11 or higher
- MySQL Server installed and running
- A MySQL database named `employee_db` must be created before starting the application

Setup instructions:

Create a virtual environment:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root with the following content:
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=employee_db

Run the application:
uvicorn app.main:app --reload

The application will start on:
http://127.0.0.1:8000

API documentation (Swagger UI) is available at:
http://127.0.0.1:8000/docs

Available API endpoints:

POST /employees
Creates a new employee record.

GET /employees/{id}
Fetches an employee by ID.

PUT /employees/{id}
Updates employee details. Partial updates are supported.

DELETE /employees/{id}
Performs a soft delete by setting is_active to false.

GET /employees?page=1&limit=10
Lists active employees with pagination support.

Additional notes:

Email field is enforced as unique.
Delete operation does not remove data from the database.
Pagination is implemented using page and limit query parameters.
Environment variables are used for database configuration.

# Employee Management System – FastAPI

A backend service built using **FastAPI** to manage employee data with full CRUD support using a **MySQL** database.  
The project follows a clean architecture and uses **SQLAlchemy ORM** for database interactions.

---

## 🚀 Features

- Create, read, update, and soft-delete employees
- Pagination support for listing employees
- Email uniqueness enforced
- Environment-based configuration
- Auto-generated API documentation (Swagger)

---

## 🛠 Technology Stack

- Python 3.11
- FastAPI
- SQLAlchemy (ORM)
- MySQL Server
- Uvicorn
- Pydantic

---

## 📁 Project Structure

```text
employee_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routes/
│       └── employees.py
├── .env
├── venv/
└── README.md
```
---

## Database Details

- **Database Name:** `employee_db`
- **Table Name:** `employees`

### Table Schema

| Column Name | Type           | Description                     |
|------------|----------------|---------------------------------|
| id         | INT            | Primary key, auto-increment     |
| name       | VARCHAR(100)   | Employee name                   |
| email      | VARCHAR(100)   | Unique email                    |
| department | VARCHAR(50)    | Department name                 |
| salary     | DECIMAL(10,2)  | Employee salary                 |
| is_active  | BOOLEAN        | Soft delete flag                |
| created_at | DATETIME       | Record creation timestamp       |

---

## ✅ Prerequisites

- Python **3.11 or higher**
- MySQL Server installed and running
- MySQL database **`employee_db`** created beforehand

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
## 2. Install Dependencies

```bash
pip install -r requirements.txt
```
## 3. Create .env File

Create a .env file in the project root with the following content:
```text
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=employee_db
```
## 4. Run the Application
```bash
uvicorn app.main:app --reload
```

## 🌐 Application URLs

- **Base URL:**  
  http://127.0.0.1:8000

- **Swagger API Docs:**  
  http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

### ➕ Create Employee
**POST** `/employees`  
Creates a new employee record.

---

### 🔍 Get Employee by ID
**GET** `/employees/{id}`  
Fetches an employee by ID.

---

### ✏️ Update Employee
**PUT** `/employees/{id}`  
Updates employee details.  
✔ Partial updates supported.

---

### 🗑 Soft Delete Employee
**DELETE** `/employees/{id}`  
Marks employee as inactive (`is_active = false`).

---

### 📄 List Employees
**GET** `/employees?page=1&limit=10`  
Returns active employees with pagination.

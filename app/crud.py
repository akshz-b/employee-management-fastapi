from sqlalchemy.orm import Session
from .models import Employee
from .schemas import EmployeeCreate, EmployeeUpdate

def create_employee(db: Session, emp: EmployeeCreate):
    employee = Employee(**emp.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(
        Employee.id == emp_id,
        Employee.is_active == True
    ).first()

def update_employee(db: Session, emp_id: int, emp: EmployeeUpdate):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        return None

    for key, value in emp.model_dump(exclude_unset=True).items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return employee


def soft_delete_employee(db: Session, emp_id: int):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        return None

    employee.is_active = False
    db.commit()
    return employee


def list_employees(db: Session, skip: int, limit: int):
    return db.query(Employee).filter(
        Employee.is_active == True
    ).offset(skip).limit(limit).all()

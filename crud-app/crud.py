from sqlalchemy.orm import Session
import models , schemas

def get_employees(db: Session):
    """Retrieve all employees from the database."""
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    """Retrieve a single employee by ID."""
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first() 
    # .first() : This method returns the first result of the query or None if no results are found.
    # .all() : This method retrieves all results of the query as a list. (TEST it first)


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    """Create a new employee in the database."""
    db_employee = models.Employee(name=employee.name, email=employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)  # to get the generated ID and other defaults.
    return db_employee

def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    """Update an existing employee in the database."""
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    """Delete an employee from the database."""
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
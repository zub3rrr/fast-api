import models, schemas,crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine , Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" WITHOUT YIELD :
[Start request]
   ↓
Call get_db()
   ↓
Session created
   ↓
return db
   ↓
(route runs CRUD)
   ↓
Session still open -> Over time → multiple open sessions → memory leaks / connection pool overflow.

"""

""" WITH YIELD :
[Start request]
   ↓
Call get_db()
   ↓
Session created
   ↓
yield db  → route handler uses it
   ↓
(route runs CRUD)
   ↓
request done → control returns to get_db()
   ↓
finally: db.close()
   ↓
Session closed properly

"""

#Endpoints Creation
#create employee
@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

#get all employees
@app.get("/employees", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

#get employee by id
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#update employee
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#delete employee
@app.delete("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

"""

#delete employee - Alternative
@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}

"""

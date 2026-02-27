from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import schemas
import models

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=schemas.EmployeeResponse)
def create(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@app.get("/employees/")
def read(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.delete("/employees/{emp_id}")
def delete(emp_id: str, db: Session = Depends(get_db)):
    return crud.delete_employee(db, emp_id)
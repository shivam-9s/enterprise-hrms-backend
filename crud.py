from sqlalchemy.orm import Session
import models
import schemas

def create_employee(db: Session, emp: schemas.EmployeeCreate):
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_employees(db: Session):
    return db.query(models.Employee).all()

def delete_employee(db: Session, emp_id: str):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    db.delete(emp)
    db.commit()
    return {"message": "Deleted"}

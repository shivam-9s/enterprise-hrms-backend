from pydantic import BaseModel
from datetime import date
from uuid import UUID


class EmployeeCreate(BaseModel):
    organization_id: str
    employee_code: str
    first_name: str
    last_name: str
    email: str
    hire_date: date
    employment_type: str | None = None
    phone: str | None = None
    status: str = "Active"


class EmployeeResponse(BaseModel):
    id: UUID
    organization_id: UUID
    employee_code: str
    first_name: str
    last_name: str
    email: str
    hire_date: date
    employment_type: str | None = None
    phone: str | None = None
    status: str

    class Config:
        from_attributes = True

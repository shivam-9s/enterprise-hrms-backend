from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy import DateTime
import uuid
from database import Base


# 🔹 ADD THIS MODEL (Required for FK to work)
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(200), nullable=False)
    domain = Column(String(200), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())


# 🔹 Your Employee Model
class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    organization_id = Column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id"),
        nullable=False
    )

    employee_code = Column(String(50), unique=True, nullable=False)

    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)

    email = Column(String(200), unique=True, nullable=False)

    hire_date = Column(Date, nullable=False)

    employment_type = Column(String(50))
    phone = Column(String(20))

    status = Column(String(50), default="Active")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

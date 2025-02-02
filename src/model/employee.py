from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .declarative_base import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=True)
    datetime = Column(DateTime, nullable=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('job.id'), nullable=True)
 
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .declarative_base import Base
import csv

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=True)
    datetime = Column(DateTime, nullable=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('job.id'), nullable=True)

    @classmethod
    def load_file(cls, session):
        with open('src/data/hired_employees.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                id, name, hire_date, department, job = row
                if hire_date: 
                    hire_date=datetime.strptime(hire_date, "%Y-%m-%dT%H:%M:%SZ")
                else:
                    hire_date = None    
                employee = Employee(id=int(id), name=name, datetime=hire_date, department_id=department, job_id=job)
                session.add(employee)
            session.commit()
 
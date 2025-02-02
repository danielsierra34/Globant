import csv
from flask import Flask
from datetime import datetime
from src.model.department import Department
from src.model.employee import Employee
from src.model.job import Job
from src.model.declarative_base import Session, engine, Base
from routes import api_routes

if __name__ == '__main__':
   Base.metadata.create_all(engine)

   session = Session()

   # Función para cargar los departamentos desde el CSV
def load_departments():
    with open('src/data/departments.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id, name = row
            department = Department(id=int(id), department=name)
            session.add(department)

# Función para cargar los trabajos desde el CSV
def load_jobs():
    with open('src/data/jobs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id, name = row
            job = Job(id=int(id), job=name)
            session.add(job)

# Función para cargar los empleados desde el CSV
def load_employees():
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

# Cargar los datos
load_departments()
load_jobs()
load_employees()
 

session.commit()
session.close()
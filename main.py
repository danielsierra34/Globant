from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.model.department import Department
from src.model.employee import Employee
from src.model.metrics import Metrics
from src.model.job import Job
from src.model.declarative_base import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/departments/load")
def departments_load(db: Session = Depends(get_db)):
    Department.load_file(db)
    return {"message": "Se cargaron los Departaments"}

@app.get("/employees/load")
def employees_load(db: Session = Depends(get_db)):
    Employee.load_file(db)
    return {"message": "Se cargaron los Employees"}

@app.get("/jobs/load")
def jobs_load(db: Session = Depends(get_db)):
    Job.load_file(db)
    return {"message": "Se cargaron los Jobs"}

@app.get("/all/load")
def all_load(db: Session = Depends(get_db)):
    Department.load_file(db)
    Employee.load_file(db)
    Job.load_file(db)
    return {"message": "Se cargaron Departments, Jobs y Employees"}

@app.get("/metrics/top_hiring_departments")
async def get_top_hiring_departments(request: Request, db: Session = Depends(get_db)):
    data = Metrics.get_top_hiring_departments(db)
    return templates.TemplateResponse("top_hiring_departments.html",{
        "request": request,
        "departments": data
        })

@app.get("/metrics/employee_hires_by_department_and_quarter")
async def get_employee_hires_by_department_and_quarter(request: Request, db: Session = Depends(get_db)):
    data = Metrics.get_employee_hires_by_department_and_quarter(db)
    return templates.TemplateResponse("employee_hires_by_department_and_quarter.html", {
        "request": request,
         "data": data
         })
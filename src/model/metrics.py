from sqlalchemy import case, func, extract
from sqlalchemy.orm import Session
from src.model.department import Department
from src.model.employee import Employee
from src.model.job import Job
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class Metrics:
    def __init__(self, db: Session):
        self.db = db

    @classmethod
    def get_top_hiring_departments(cls, session):

        hires_per_department_query = session.query(
            Department.id.label("department_id"),
            Department.department.label("department"),
            func.count(Employee.id).label("hired")
        ).join(Employee, Employee.department_id == Department.id) \
        .filter(extract('year', Employee.datetime) == 2021) \
        .group_by(Department.id)

        avg_hires_subquery = hires_per_department_query.subquery()
        avg_hires_query = session.query(
            func.avg(avg_hires_subquery.c.hired).label("avg_hires")
        ).scalar()

        if avg_hires_query is None:
            avg_hires_query = 0

        result = session.query(
            Department.id.label("id"),
            Department.department.label("department"),
            func.count(Employee.id).label("hired")
        ).join(Employee, Employee.department_id == Department.id) \
        .filter(extract('year', Employee.datetime) == 2021) \
        .group_by(Department.id, Department.department) \
        .having(func.count(Employee.id) > avg_hires_query) \
        .order_by(func.count(Employee.id).desc()) \
        .all()

        return jsonable_encoder([
            {
                "id": id,
                "department": department,
                "hired": hired
            }for id, department, hired in result
        ])
    
    @classmethod
    def get_employee_hires_by_department_and_quarter(cls, session):

        result = session.query(
            Department.department.label('department'),
            Job.job.label('job'),
            func.count(case((extract('month', Employee.datetime).in_([1, 2, 3]), Employee.id))).label("Q1"),
            func.count(case((extract('month', Employee.datetime).in_([4, 5, 6]), Employee.id))).label("Q2"),
            func.count(case((extract('month', Employee.datetime).in_([7, 8, 9]), Employee.id))).label("Q3"),
            func.count(case((extract('month', Employee.datetime).in_([10, 11, 12]), Employee.id))).label("Q4"),
        ).join(Employee, Employee.job_id == Job.id) \
        .join(Department, Employee.department_id == Department.id) \
        .filter(extract('year', Employee.datetime) == 2021) \
        .group_by(Department.department, Job.job) \
        .order_by(Department.department.asc(), Job.job.asc()) \
        .all()

        return jsonable_encoder([
            {
                "department": department,
                "job": job,
                "Q1": Q1 or 0,
                "Q2": Q2 or 0,
                "Q3": Q3 or 0,
                "Q4": Q4 or 0
            }for department, job, Q1, Q2, Q3, Q4 in result
        ])
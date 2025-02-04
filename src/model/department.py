from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base
import csv

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=False)
    department = Column(String)

    @classmethod
    def load_file(cls, session):
        with open('src/data/departments.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            session.query(Department).delete()
            for row in reader:
                id, name = row
                department = Department(id=int(id), department=name)
                session.add(department)
            session.commit()
                
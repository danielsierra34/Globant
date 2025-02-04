from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base
import csv

class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True, autoincrement=False)
    job = Column(String)
    
    @classmethod
    def load_file(cls, session):
        with open('src/data/jobs.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                id, name = row
                job = Job(id=int(id), job=name)
                session.add(job)
            session.commit()
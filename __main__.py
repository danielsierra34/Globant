from src.model.department import Department
from src.model.employee import Employee
from src.model.job import Job
from src.model.declarative_base import engine, Base
import uvicorn

if __name__ == '__main__':
    # Crea las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    
    # Inicia el servidor Uvicorn
    #uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
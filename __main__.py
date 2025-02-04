from src.model.department import Department
from src.model.employee import Employee
from src.model.job import Job
from src.model.declarative_base import engine, Base
import uvicorn

if __name__ == '__main__':
    # Crea las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    
    # Inicia el servidor Uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=5000, reload=True)
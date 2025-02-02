from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=False)
    department = Column(String)
    #minutos = Column(Integer)
    #segundos = Column(Integer)
    #compositor = Column(String)
    #albumes = relationship('Album', secondary='album_cancion')
    #interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')
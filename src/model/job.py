from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True, autoincrement=False)
    job = Column(String)
    #minutos = Column(Integer)
    #segundos = Column(Integer)
    #compositor = Column(String)
    #albumes = relationship('Album', secondary='album_cancion')
    #interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')
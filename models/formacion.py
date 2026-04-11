from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.database import Base

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": "grupo_7"}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(Integer, ForeignKey("grupo_7.personal.idPersona"))
    nivelDeFormacion = Column(String)
    tituloObtenido = Column(String)
    institucion = Column(String)
    fechaFinal = Column(Date)
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from db.database import Base

class Personal(Base):
    __tablename__ = "personal"
    __table_args__ = {"schema": "grupo_7"}

    idPersona = Column(Integer, primary_key=True, index=True)
    idCargo = Column(Integer)
    nombre = Column(String(50))
    documento = Column(String(50))
    correo = Column(String(50))
    telefono = Column(String(50))
    estado = Column(Boolean, default=True)

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": "grupo_7"}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(Integer, ForeignKey("grupo_7.personal.idPersona"))
    nivelDeFormacion = Column(String(50))
    tituloObtenido = Column(String(100))
    institucion = Column(String(100))
    fechaFinal = Column(Date)
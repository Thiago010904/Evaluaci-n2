from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Personal(Base):
    __tablename__ = "personal"
    __table_args__ = {"schema": "grupo_7"}
    
    idPersona = Column(Integer, primary_key=True, index=True)
    idCargo = Column(Integer)
    nombre = Column(String)
    documento = Column(String)
    correo = Column(String)
    telefono = Column(String)
    estado = Column(Boolean)
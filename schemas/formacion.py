from pydantic import BaseModel
from datetime import date

class FormacionBase(BaseModel):
    idPersona: int
    nivelDeFormacion: str
    tituloObtenido: str
    institucion: str
    fechaFinal: date

class FormacionCreate(FormacionBase):
    pass

class FormacionUpdate(FormacionBase):
    pass

class FormacionOut(FormacionBase):
    idFormacion: int

    class Config:
        from_attributes = True
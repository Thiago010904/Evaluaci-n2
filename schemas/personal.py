from pydantic import BaseModel

class PersonalBase(BaseModel):
    idCargo: int
    nombre: str
    documento: str
    correo: str
    telefono: str
    estado: bool

class PersonalCreate(PersonalBase):
    pass

class PersonalUpdate(PersonalBase):
    pass

class PersonalOut(PersonalBase):
    idPersona: int

    class Config:
        from_attributes = True
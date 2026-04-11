from sqlalchemy.orm import Session
from models.formacion import Formacion
from schemas.formacion import FormacionCreate, FormacionUpdate


def crear_formacion(db: Session, formacion: FormacionCreate):
    nuevo = Formacion(**formacion.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_formacion(db: Session):
    return db.query(Formacion).all()


def obtener_formacion(db: Session, id: int):
    return db.query(Formacion).filter(Formacion.idFormacion == id).first()


def actualizar_formacion(db: Session, id: int, formacion: FormacionUpdate):
    registro = db.query(Formacion).filter(Formacion.idFormacion == id).first()
    if registro:
        for key, value in formacion.dict(exclude_unset=True).items():
            setattr(registro, key, value)
        db.commit()
        db.refresh(registro)
    return registro


def eliminar_formacion(db: Session, id: int):
    registro = db.query(Formacion).filter(Formacion.idFormacion == id).first()
    if registro:
        db.delete(registro)
        db.commit()
    return registro
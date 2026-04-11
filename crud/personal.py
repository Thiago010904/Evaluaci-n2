from sqlalchemy.orm import Session
from models.personal import Personal
from schemas.personal import PersonalCreate, PersonalUpdate


def crear_personal(db: Session, personal: PersonalCreate):
    nuevo = Personal(**personal.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_personal(db: Session):
    return db.query(Personal).all()


def obtener_personal(db: Session, id: int):
    return db.query(Personal).filter(Personal.idPersona == id).first()


def actualizar_personal(db: Session, id: int, personal: PersonalUpdate):
    registro = db.query(Personal).filter(Personal.idPersona == id).first()
    if registro:
        for key, value in personal.dict(exclude_unset=True).items():
            setattr(registro, key, value)
        db.commit()
        db.refresh(registro)
    return registro


def eliminar_personal(db: Session, id: int):
    registro = db.query(Personal).filter(Personal.idPersona == id).first()
    if registro:
        db.delete(registro)
        db.commit()
    return registro
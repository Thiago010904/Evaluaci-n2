from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
import crud.personal as crud
from schemas.personal import PersonalCreate, PersonalUpdate, PersonalOut

router = APIRouter(prefix="/personal", tags=["Personal"])


@router.post("/", response_model=PersonalOut)
def crear(personal: PersonalCreate, db: Session = Depends(get_db)):
    return crud.crear_personal(db, personal)


@router.get("/", response_model=list[PersonalOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_personal(db)


@router.get("/{id}", response_model=PersonalOut)
def obtener(id: int, db: Session = Depends(get_db)):
    return crud.obtener_personal(db, id)


@router.put("/{id}", response_model=PersonalOut)
def actualizar(id: int, personal: PersonalUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_personal(db, id, personal)


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return crud.eliminar_personal(db, id)
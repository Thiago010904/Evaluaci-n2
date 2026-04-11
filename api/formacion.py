from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
import crud.formacion as crud
from schemas.formacion import FormacionCreate, FormacionUpdate, FormacionOut

router = APIRouter(prefix="/formacion", tags=["Formacion"])


@router.post("/", response_model=FormacionOut)
def crear(formacion: FormacionCreate, db: Session = Depends(get_db)):
    return crud.crear_formacion(db, formacion)


@router.get("/", response_model=list[FormacionOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_formacion(db)


@router.get("/{id}", response_model=FormacionOut)
def obtener(id: int, db: Session = Depends(get_db)):
    return crud.obtener_formacion(db, id)


@router.put("/{id}", response_model=FormacionOut)
def actualizar(id: int, formacion: FormacionUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_formacion(db, id, formacion)


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    return crud.eliminar_formacion(db, id)
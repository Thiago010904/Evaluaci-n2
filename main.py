from fastapi import FastAPI
from api.personal import router as personal_router
from api.formacion import router as formacion_router

from db.database import engine, Base
from models import personal, formacion

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(personal_router)
app.include_router(formacion_router)


from fastapi import FastAPI
from app.api.routes import food_item
from app.database.base import Base
from app.database.connection import engine

app = FastAPI()
app.include_router(food_item.router)
#Permite crear/validar si ya existe la base de datos
Base.metadata.create_all(bind=engine)
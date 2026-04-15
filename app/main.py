from fastapi import FastAPI
from app.api.routes import food_item,user
from app.database.base import Base
from app.database.connection import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#Permite crear/validar si ya existe la base de datos
Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(food_item.router)
app.include_router(user.router)
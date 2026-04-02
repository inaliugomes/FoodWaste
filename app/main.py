from fastapi import FastAPI
from app.api.routes import food_item
from app.database.base import Base
from app.database.connection import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(food_item.router)
from fastapi import FastAPI
from app.api.routes import food_item

app = FastAPI()

app.include_router(food_item.router)
from fastapi import FastAPI
from app.api.routes import food_item, user, auth
from app.database.base import Base
from app.database.connection import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#Creates the database tables if they do not exist yet
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
app.include_router(auth.router)
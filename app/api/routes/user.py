from fastapi import Depends,APIRouter,Query
from sqlalchemy.orm import Session
from app.crud.user import create_user
from app.database.connection import get_db
from app.schemas.user import UserItemResponse, UserCreate

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("/", response_model=UserItemResponse)
def create(user:UserCreate, db:Session = Depends(get_db)):
    return create_user(user,db)
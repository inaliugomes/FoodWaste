from fastapi import Depends,APIRouter,Query
from sqlalchemy.orm import Session
from app.crud.user import create_user,get_all_users,get_user_by_id,delete_user_by_id
from app.database.connection import get_db
from app.schemas.user import UserItemResponse, UserCreate,UserListResponse

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("/", response_model=UserItemResponse)
def create(user:UserCreate, db:Session = Depends(get_db)):
    return create_user(user,db)

@router.get("/", response_model=UserListResponse)
def get_all_user(db:Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserItemResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    return get_user_by_id(user_id,db)

@router.delete("/{user_id}", response_model=UserItemResponse)
def delete_user(user_id:int, db:Session = Depends(get_db)):

    return delete_user_by_id(user_id,db)
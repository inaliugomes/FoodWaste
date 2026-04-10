from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.user import UserCreate

def create_user(user:UserCreate,db:Session):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
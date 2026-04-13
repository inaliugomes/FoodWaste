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

def get_all_users(db:Session):

    users =  db.query(User).all()
    total = len(users)
    if users:
        return {"users":users, "total":total}
    else:
        return {"users":[], "total":total}


def get_user_by_id(user_id:int, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user":user}

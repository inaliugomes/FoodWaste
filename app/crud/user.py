from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.user import UserCreate,UserUpdate

def create_user(user:UserCreate,db:Session):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db:Session):

    users =  db.query(User).all()
    total = db.query(User).count()
    if users:
        return {"total":total,"users":users}
    else:
        return {"total":total, "users":[]}


def get_user_by_id(user_id:int, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_by_id(user_id:int, db:Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.foodItems:
        raise HTTPException(status_code=409, detail="This user has Food Items associated and cannot be deleted")
    db.delete(user)
    db.commit()
    return {"mensage":"User deleted successfully"}

def update_user_by_id(user_id:int,user:UserUpdate,db:Session):

    user_item = db.query(User).filter(User.id == user_id).first()

    if not user_item:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user_item, key, value)
    db.commit()
    db.refresh(user_item)

    return user_item

from fastapi import HTTPException
from sqlalchemy.orm import Session, session
from app.database.models import  FoodItem
from app.schemas.food_item import FoodItemCreate

#Create Element
def create_food_item(db:Session,item:FoodItemCreate):
    db_item = FoodItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#Search for all element
def get_all_food_items(db:Session):
    return db.query(FoodItem).all()

#Get element By ID
def get_food_item_by_id(db:Session,food_item_id:int):
    food_item = db.query(FoodItem).filter(FoodItem.id == food_item_id).first()
    if not food_item:
        raise HTTPException(status_code=404, detail="FoodItem not found")

    return food_item

def delete_food_item_by_id(db:Session,food_item_id:int):
    food_item = db.query(FoodItem).filter(FoodItem.id == food_item_id).first()
    if not food_item:
        raise HTTPException(status_code=404, detail="FoodItem not found")
    db.delete(food_item)
    db.commit()
    return food_item



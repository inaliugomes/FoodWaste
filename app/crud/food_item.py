from sqlalchemy.orm import Session
from app.database.models import  FoodItem
from app.schemas.food_item import FoodItemCreate

def create_food_item(db:Session,item:FoodItemCreate):
    db_item = FoodItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_food_items(db:Session):
    return db.query(FoodItem).all()
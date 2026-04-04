from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import FoodItem
from app.schemas.food_item import FoodItemCreate, FoodItemResponse
from app.crud.food_item import create_food_item,get_all_food_items,get_food_item_by_id,delete_food_item_by_id

router = APIRouter(
    prefix="/food_item",
    tags=["Food Item"]
)

@router.post("/",response_model=FoodItemResponse)
def create(item:FoodItemCreate, db:Session=Depends(get_db)):
    return create_food_item(db,item)


@router.get("/",response_model=list[FoodItemResponse])
def get_all(db:Session=Depends(get_db)):
    return get_all_food_items(db)

@router.get("/{food_item_id}",response_model=FoodItemResponse)
def get_food(food_item_id:int,db:Session=Depends(get_db)):
    return get_food_item_by_id(db,food_item_id)

@router.delete("/{food_item_id}",response_model=FoodItemResponse)
def delete(food_item_id:int,db:Session=Depends(get_db)):
    return delete_food_item_by_id(db,food_item_id)
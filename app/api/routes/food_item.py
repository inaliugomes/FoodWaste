from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import FoodItem
from app.schemas.food_item import FoodItemCreate, FoodItemUpdate, FoodItemResponse
from app.crud.food_item import create_food_item

router = APIRouter(
    prefix="/food_item",
    tags=["Food Item"]
)

@router.post("/",response_model=FoodItemResponse)
def create(item:FoodItemCreate, db:Session=Depends(get_db)):
    return create_food_item(db,item)
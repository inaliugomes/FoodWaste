from fastapi import Depends , APIRouter,Query
from sqlalchemy.orm import Session
from typing import Annotated
from app.crud.auth import get_current_user
from app.database.models import User
from app.core.enums import FoodNameEnum, CategoryEnum
from app.database.connection import get_db
from app.schemas.food_item import FoodItemCreate, FoodItemResponse, FoodItemUpdate, FoodItemListResponse
from app.crud.food_item import create_food_item,get_all_food_items,get_food_item_by_id,delete_food_item_by_id,update_food_item_by_id

router = APIRouter(
    prefix="/food_item",
    tags=["Food Item"]
)

@router.post("/",response_model=FoodItemResponse)
def create(item:FoodItemCreate, db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_food_item(db,item,current_user)


@router.get("/", response_model=FoodItemListResponse)
def get_all(skip:Annotated[int,Query(ge=0)]=0,
            limit:Annotated[int,Query(ge=0,le=10)]=10,
            food_name:Annotated[FoodNameEnum | None,Query()]=None,
            food_category:Annotated[CategoryEnum |None,Query()]=None,
            food_quantity:Annotated[int |None ,Query()]=None,
            db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_all_food_items(db,skip=skip,limit=limit,
                              food_name=food_name,
                              food_category=food_category,
                              food_quantity=food_quantity)


@router.get("/{food_item_id}",response_model=FoodItemResponse)
def get_food(food_item_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_food_item_by_id(db,food_item_id)

@router.delete("/{food_item_id}")
def delete(food_item_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return delete_food_item_by_id(db,food_item_id,current_user)


@router.put("/{food_item_id}",response_model=FoodItemResponse)
def update(food_item_id:int,item:FoodItemUpdate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return update_food_item_by_id(db,food_item_id,item,current_user)
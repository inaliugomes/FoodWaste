from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.enums import  FoodNameEnum,CategoryEnum
from app.database.models import  FoodItem
from app.database.models import User
from app.schemas.food_item import FoodItemCreate,FoodItemUpdate

#Create Element
def create_food_item(db:Session,item:FoodItemCreate,current_user:User):
    db_item = FoodItem(**item.model_dump(), user_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#Search for all element
def get_all_food_items(
                       db:Session,
                       skip:int=0,
                       limit:int=10,
                       food_name:FoodNameEnum |None=None,
                       food_category:CategoryEnum |None =None,
                       food_quantity:int |None=None
                       ):
    query = db.query(FoodItem)
    if food_name:
        query = query.filter(FoodItem.name == food_name)

    if food_category:
        query = query.filter(FoodItem.category == food_category)

    if food_quantity is not None:
        query = query.filter(FoodItem.quantity >= food_quantity)

    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return {"total": total, "items": items}
#Get element By ID
def get_food_item_by_id(db:Session,food_item_id:int):
    food_item = db.query(FoodItem).filter(FoodItem.id == food_item_id).first()
    if not food_item:
        raise HTTPException(status_code=404, detail="FoodItem not found")

    return food_item

def delete_food_item_by_id(db:Session,food_item_id:int,current_user:User):
    food_item = db.query(FoodItem).filter(FoodItem.id == food_item_id).first()
    if not food_item:
        raise HTTPException(status_code=404, detail="FoodItem not found")

    if food_item.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can't delete a item that does not belong to you")

    db.delete(food_item)
    db.commit()
    return {"mensage":"FoodItem deleted successfully"}


def update_food_item_by_id(db:Session,food_item_id:int,item:FoodItemUpdate,current_user:User):
    food_item = db.query(FoodItem).filter(FoodItem.id == food_item_id).first()

    if not food_item:
        raise HTTPException(status_code=404, detail="FoodItem to updade not found")

    if food_item.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can't update a item that does not belong to you")
    #transforms the python object into a dictionary

    update_data =  item.model_dump(exclude_unset=True)
    #Listener, que siempre esta escuchando y validando los cambios
    for key, value in update_data.items():
        setattr(food_item, key, value)

    db.commit()
    db.refresh(food_item)

    return food_item
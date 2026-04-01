from pydantic import BaseModel , ConfigDict , Field
from datetime import datetime
from typing import Optional
from app.database.models import FoodNameEnum ,CategoryEnum


class FoodItemBase(BaseModel):
    name: FoodNameEnum
    quantity:int = Field(...,ge=0)
    weight_in_grams : float = Field(...,ge=0)
    category:CategoryEnum


class FoodItemCreate(FoodItemBase):
    pass

class FoodItemResponse(FoodItemBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    created_at:datetime

class FoodItemUpdate(BaseModel):
    name: Optional[FoodNameEnum] = None
    quantity: Optional[int] = Field(None,ge=0)
    weight_in_grams: Optional[float] = Field(None,gt=0)
    category:Optional[CategoryEnum] = None
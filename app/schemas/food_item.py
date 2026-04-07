from pydantic import BaseModel , ConfigDict , Field
from datetime import datetime
from typing import Optional
from app.database.models import FoodNameEnum ,CategoryEnum

#Valido para que FASTAPI sepa que tipo de datos estamos esperando recibir
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
    model_config = ConfigDict(from_attributes=True)
    name: Optional[FoodNameEnum] = None
    quantity: Optional[int] = Field(None,ge=0)
    weight_in_grams: Optional[float] = Field(None,gt=0)
    category:Optional[CategoryEnum] = None

class FilterParams(FoodItemResponse):
    foods:list[FoodItemBase]
    limit: int = Field(100,ge=0)
    skip: int = Field(0,ge=0)
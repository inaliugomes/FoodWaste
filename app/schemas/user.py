
from pydantic import BaseModel , ConfigDict, Field
from datetime import datetime
from typing import Optional


class User(BaseModel):
    name:str = Field(min_length=4)
    unique_Code:int = Field(...,ge=1000,le=9999)

class UserCreate(User):
    pass

class UserItemResponse(User):
    model_config = ConfigDict(from_attributes=True)
    id:int
    created_at: datetime

class UserUpdate(BaseModel):
    name : Optional[str] =None
    unique_Code : Optional[int] =Field(None,ge=1000,le=9999)
class UserListResponse(BaseModel):
    total:int
    users:list[UserItemResponse]



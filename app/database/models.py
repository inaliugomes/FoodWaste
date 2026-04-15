from sqlalchemy import DateTime, Integer, Float,String,ForeignKey
from sqlalchemy import Enum as SQLAEnum
from datetime import datetime
from app.database.base import Base
from app.core.enums import  FoodNameEnum, CategoryEnum
from sqlalchemy.orm import Mapped ,relationship
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String,nullable=False)
    unique_Code:Mapped[int] = mapped_column(Integer,nullable=False,unique=True)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow,nullable=False)
    foodItems : Mapped[list["FoodItem"]] = relationship("FoodItem",back_populates="user")

# It is responsable to transform our Class into a SQLTABLE
class FoodItem(Base):
    __tablename__ = "food_item"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[FoodNameEnum] = mapped_column(SQLAEnum(FoodNameEnum),nullable=False)
    quantity:Mapped[int] = mapped_column(Integer,nullable=False)
    weight_in_grams: Mapped[float] = mapped_column(Float, nullable=True)
    category : Mapped[CategoryEnum] = mapped_column(SQLAEnum(CategoryEnum), nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow,nullable=False)
    user_id:Mapped[int]= mapped_column(Integer,ForeignKey('user.id'),nullable=False)
    user : Mapped[User] = relationship("User",back_populates="foodItems")

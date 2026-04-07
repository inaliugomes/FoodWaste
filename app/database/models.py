from sqlalchemy import DateTime, Integer, Float,String
from sqlalchemy import Enum as SQLAEnum
from datetime import datetime
from app.database.base import Base
from app.core.enums import  FoodNameEnum, CategoryEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


# It is responsable to transform our Class into a SQLTABLE
class FoodItem(Base):
    __tablename__ = "food_item"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[FoodNameEnum] = mapped_column(SQLAEnum(FoodNameEnum),nullable=False)
    quantity:Mapped[int] = mapped_column(Integer,nullable=False)
    weight_in_grams: Mapped[float] = mapped_column(Float, nullable=True)
    category : Mapped[CategoryEnum] = mapped_column(SQLAEnum(CategoryEnum), nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow,nullable=False)



class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String,nullable=False)

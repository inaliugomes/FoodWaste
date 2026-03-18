from sqlalchemy import DateTime, Integer, String, Float
from sqlalchemy import Enum as SQLAEnum
from datetime import datetime
from app.database.base import Base
from enum import Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

#Meu classe ENUM para que el utilizado solo puede eligir destas opciones
class FoodNameEnum(str,Enum):
    lechuga = "Lechuga"
    tomate = "Tomate"
    cebolla = "Cebolla"
    arroz = "Arroz"
    alubias = "Alubias"
    tiras = "Tiras"
    pollo = "Pollo"

class CategoryEnum(str,Enum):
    verdura = "Verdura"
    pollo = "Pollo"
    organico = "Organico"

#Meu mis classes de datos
class FoodItem(Base):
    __tablename__ = "food_item"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[FoodNameEnum] = mapped_column(SQLAEnum(FoodNameEnum),nullable=False)
    quantity:Mapped[int] = mapped_column(Integer,nullable=True)
    weight_in_grams: Mapped[float] = mapped_column(Float, nullable=True)
    category : Mapped[CategoryEnum] = mapped_column(SQLAEnum(CategoryEnum), nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow,nullable=False)


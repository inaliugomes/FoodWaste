from app.database.connection import SessionLocal,engine
from app.database.models import FoodItem,FoodNameEnum,CategoryEnum
from app.database.base import Base

Base.metadata.create_all(engine)

db = SessionLocal()

item = FoodItem(
    name=FoodNameEnum.pollo,
    quantity=20,
    weight_in_grams=200.0,
    category=CategoryEnum.pollo
)
db.add(item)
db.commit()
db.refresh(item)

items = db.query(FoodItem).all()
for item in items:
    print(item.id, item.name, item.quantity, item.weight_in_grams, item.category)
db.close()
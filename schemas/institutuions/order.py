from pydantic import BaseModel
from schemas.institutuions.food import FoodModel
from typing import List

class OrderModelItem(BaseModel):
    food: FoodModel
    quantity: int

class OrderModel(BaseModel):
    orders_items: List[OrderModelItem]
    
    

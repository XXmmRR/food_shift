from pydantic import BaseModel
from schemas.institutuions.food import FoodModel
from typing import List

class OrderModelItem(BaseModel):
    food: str
    quantity: int

class OrderModel(BaseModel):
    orders_items: List[OrderModelItem]
    
    

from pydantic import BaseModel
from schemas.institutuions.food import FoodModel
from typing import List

class OrderItem(BaseModel):
    food: FoodModel
    quantity: int

class Order:
    orders: List[OrderItem]
    
    

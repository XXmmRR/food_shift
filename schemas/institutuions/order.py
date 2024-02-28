from pydantic import BaseModel
from schemas.institutuions.food import FoodModel
from typing import List

class CreateOrder(BaseModel):
    food: str
    quantity: int

class CreateOrderModel(BaseModel):
    pass

class OrderModelItem(BaseModel):
    food: FoodModel
    quantity: int

class OrderModel(BaseModel):
    order_items: List[OrderModelItem]
    
    

from pydantic import BaseModel
from schemas.institutuions.food import FoodModel
from typing import List
from schemas.institutuions.food import PyObjectId

class CreateOrder(BaseModel):
    food: str
    quantity: int

class CreateOrderModel(BaseModel):
    order_items: List[CreateOrder]

class OrderModelItem(BaseModel):
    food: FoodModel
    quantity: int

class OrderModel(BaseModel):
    id: PyObjectId
    order_items: List[OrderModelItem]
    
    

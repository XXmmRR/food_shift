from pydantic import BaseModel, Field
from schemas.institutuions.food import FoodModel
from typing import List
from schemas.institutuions.food import PyObjectId

class CreateOrder(BaseModel):
    food: str = Field(min_length=1, max_length=30)
    quantity: int = Field(ge=1)

class CreateOrderModel(BaseModel):
    order_items: List[CreateOrder]

class OrderModelItem(BaseModel):
    food: FoodModel
    quantity: int

class OrderModel(BaseModel):
    id: PyObjectId
    order_items: List[OrderModelItem]
    
class OrderUpdate(BaseModel):
    order_items: List[OrderModelItem]

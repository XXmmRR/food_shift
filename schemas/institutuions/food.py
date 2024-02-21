from pydantic import BaseModel
from typing import Optional

class FoodModel(BaseModel):
    name: str
    decription: str
    price: int


class FoodeCreate(FoodModel):
    active: bool
    
    
class FoodOut(FoodModel):
    image: Optional[str] = None
    
    
class FoodUpdate(FoodeCreate):
    pass



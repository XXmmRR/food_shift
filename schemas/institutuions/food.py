from pydantic import BaseModel
from typing import Optional

class FoodModel(BaseModel):
    name: str
    description: str
    price: int


class FoodeCreate(FoodModel):
    active: bool
    
    
class FoodOut(FoodModel):
    image: Optional[str|None] = None
    
    
class FoodUpdate(FoodeCreate):
    pass



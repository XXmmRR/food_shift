from pydantic import BaseModel
from schemas.user.users import UserOut
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class AddressCreate(BaseModel):
    name: str
    lat: float
    lon: float
    orient: str
    
class AddressOut(AddressCreate):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

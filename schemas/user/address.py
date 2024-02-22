from pydantic import BaseModel
from schemas.user.users import UserOut
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator
from schemas.institutuions.food import PyObjectId


class AddressCreate(BaseModel):
    name: str
    lat: float
    lon: float
    orient: str


class AddressOut(AddressCreate):
    id: PyObjectId

from pydantic import BaseModel
from schemas.institutuions.food import PyObjectId


class AddressCreate(BaseModel):
    name: str
    lat: float
    lon: float
    orient: str


class AddressOut(AddressCreate):
    id: PyObjectId

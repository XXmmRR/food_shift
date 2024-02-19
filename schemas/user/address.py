from pydantic import BaseModel
from schemas.user.users import UserOut

class AddressCreate(BaseModel):
    name: str
    lat: float
    lon: float
    orient: str
    user: UserOut
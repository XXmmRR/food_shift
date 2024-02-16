from beanie import Document, Indexed, init_beanie, Link
from typing import List, Optional
from datetime import datetime
from pydantic import EmailStr

class Address(Document):
    lat: float
    lon: float
    name: str
    orient: str


class User(Document):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str
    user_type: str = 'client'
    disabled: Optional[bool] = None
    email_confirmed_at: Optional[datetime] = None 
    favorites: Optional[List[Link['Institution']]] = None
    address: Optional[List[Link[Address]]] = None



class Tag(Document):
    tag_name: str
    draft: bool


class Rating(Document):
    starts: float
    user: Link[User]
    institution: Link['Institution']    


class Institution(Document):
    name: str
    image: Optional[str] = None
    description: str
    owner: Link[User] 
    tags: List[Link[Tag]] = None
    

class Food(Document):
    name: str
    description: str
    image: str
    price: int
    draft: bool
    institution: Link[Institution]
    
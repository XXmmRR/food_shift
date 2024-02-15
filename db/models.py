from beanie import Document, Indexed, init_beanie, Link
from typing import List
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
    user_type: str
    favorites: List[Link['Institution']]
    address: List[Link[Address]]



class Tag(Document):
    tag_name: str
    draft: bool


class Rating(Document):
    starts: float
    user: Link[User]
    institution: Link['Institution']    


class Institution(Document):
    name: Indexed(str)
    image: str
    description: str
    owner: Link[User]
    tags: List[Link[Tag]]
    

class Food(Document):
    name: str
    description: str
    image: str
    price: int
    draft: bool
    institution: Link[Institution]
    
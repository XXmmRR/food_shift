from beanie import Document, Indexed, init_beanie, Link
from typing import List, Optional
from datetime import datetime
from pydantic import EmailStr
from beanie import Indexed, BackLink
from pydantic import Field


class User(Document):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str
    user_type: str = "client"
    disabled: Optional[bool] = None
    email_confirmed_at: Optional[datetime] = None
    favorites: Optional[List[Link["Institution"]]] = None


class Address(Document):
    lat: float
    lon: float
    name: str
    orient: str
    user: Link[User]


class Tag(Document):
    tag_name: str
    draft: bool


class Rating(Document):
    starts: float
    user: Link[User]
    institution: Link["Institution"]


class Institution(Document):
    InstitutionName: Indexed(str, unique=True)
    image: Optional[str] = None
    description: str
    owner: Link[User]
    tags: Optional[List[Link[Tag]]] = None


class Food(Document):
    name: str
    description: str
    image: str
    price: int
    active: bool
    institution: Link[Institution]

from beanie import Document, Indexed, Link
from typing import List, Optional
from datetime import datetime
from pydantic import EmailStr
from beanie import Indexed, BackLink
from pydantic import Field


class Address(Document):
    lat: float
    lon: float
    name: str
    orient: str
    user: Link["User"]


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
    addresses: Optional[List[BackLink[Address]]] = Field(original_field="user")
    orders: Optional[List[BackLink['Order']]] = Field(original_field='user')


class Tag(Document):
    tag_name: str
    draft: bool


class Rating(Document):
    stars: float
    user: Link[User]
    institution: Link["Institution"]


class Institution(Document):
    InstitutionName: Indexed(str, unique=True)
    image: Optional[str] = None
    description: str
    avg_cooking_time: str
    owner: Link[User]
    tags: Optional[List[Link[Tag]]] = None
    ratings: Optional[List[BackLink[Rating]]] = Field(original_field="institution")
    foods: Optional[List[BackLink["Food"]]] = Field(original_field="institution")


class Category(Document):
    name: str

class Ingritient(Document):
    name: str
    photo: str

class Ingridients(Document):
    name: str
    image: str  


class Food(Document):
    name: str
    description: str
    image: Optional[str] = None
    price: int
    draft: bool
    calories: float
    weight: float
    avg_cooking_time: float
    ingritients: Optional[List[Link[Ingritient]]]
    institution: Link[Institution]
    category: Link[Category]
    ingritients: List[Link[Ingridients]]
    

class OrderItem(Document):
    food: Link[Food]
    quantity: int
    user: Link[User]


class Order(Document):
    order_items: List[Link[OrderItem]]
    user: Link[User]
    institution: Link[Institution]
    price: int


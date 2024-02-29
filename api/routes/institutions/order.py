"""Order router."""

from fastapi import APIRouter, Depends, Security
from fastapi import APIRouter, HTTPException
from db.models import Order, OrderItem, Food
from typing import List
from pymongo.errors import DuplicateKeyError
from schemas.institutuions.order import (
    OrderModelItem,
    OrderModel,
    CreateOrderModel
)
from core.jwt import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from api.depends.user.current_user import current_user
from utils.pydantic_encoder import encode_input
from schemas.institutuions.order import OrderModel
from api.depends.institution.current_institution import current_institution
from db.models import User
from beanie.operators import And


router = APIRouter(prefix="/order", tags=["Order"])

@router.post('/{institution_name}', response_model=OrderModel)
async def create_order(
                       order: CreateOrderModel,
                       institution=Depends(current_institution),
                       auth: JwtAuthorizationCredentials = Security(access_security),
                       user: User = Depends(current_user)
                       ):
    orders = []
    price = 0
    for i in order.order_items:
        food = await Food.find_one(And(Food.name==i.food, Food.institution.id==institution.id,), fetch_links=True)
        price += food.price
        order_obj = OrderItem(food=food, quantity=i.quantity, user=user)
        orders.append(order_obj)
        await order_obj.save()
    order = Order(order_items=orders, user=user, institution=institution, price=price)
    await Order.insert(order)
    return order


"""Order router."""

from fastapi import APIRouter, HTTPException, UploadFile, Depends
from fastapi import APIRouter, HTTPException
from db.models import Order, OrderItem
from typing import List
from pymongo.errors import DuplicateKeyError
from schemas.institutuions.order import (
    OrderModelItem,
    OrderModel,
)

from utils.pydantic_encoder import encode_input
from api.depends.institution.current_institution import current_institution



router = APIRouter(prefix="/order", tags=["Order"])

@router.post('/{institution_name}')
async def create_order(
                       order: OrderModel,
                       institution=Depends(current_institution),
                       ):
    for i in order.orders_items:
        order_obj = OrderItem(**i)
        await order_obj.save()
        
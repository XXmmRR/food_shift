'''Order router'''
from fastapi import APIRouter, Depends
from fastapi import APIRouter
from typing import List
from db.models import Order, OrderItem
from schemas.institutuions.category import Category as CategorySchema
from api.depends.institution.current_institution import current_institution

router = APIRouter(prefix="/order", tags=["Order"])



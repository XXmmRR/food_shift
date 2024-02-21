"""Food router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from fastapi import APIRouter, HTTPException, status
from db.models import Tag as TagDoc
from typing import List
from pymongo.errors import DuplicateKeyError
from schemas.institutuions.food import (
    FoodeCreate,
    FoodOut,
    FoodUpdate
)
from db.models import Food, Institution
from utils.pydantic_encoder import encode_input
import aiofiles



router = APIRouter(prefix="/food", tags=["Food"])


@router.post('/{institution_name}', response_model=FoodOut)
async def create_food(
                    institution_name: str,
                    food_data: FoodeCreate,
                    ):
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    food = Food(name=food_data.name, description=food_data.decription, price=food_data.price, active=food_data.active, institution=institution)
    await food.insert()
    return food



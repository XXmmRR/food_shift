"""Food router."""

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from db.models import Institution, User
from schemas.user.users import UserAuth
from fastapi import APIRouter, HTTPException, status
from db.models import Tag as TagDoc
from typing import List
from pymongo.errors import DuplicateKeyError
from schemas.institutuions.food import FoodeCreate, FoodOut, FoodUpdate
from db.models import Food, Institution
from utils.pydantic_encoder import encode_input
import aiofiles
from api.depends.institution.current_institution import current_institution

router = APIRouter(prefix="/food", tags=["Food"])


@router.post("/{institution_name}", response_model=FoodOut)
async def create_food(
    institution_name: str,
    food_data: FoodeCreate,
    institution: Institution = Depends(current_institution),
):
    food = Food(
        name=food_data.name,
        description=food_data.description,
        price=food_data.price,
        active=food_data.active,
        institution=institution,
        draft=food_data.draft,
    )
    await Food.create(food)
    return food


@router.get("/{institution_name}", response_model=List[FoodOut])
async def get_food_by_institution(
    institution_name: str, institution: Institution = Depends(current_institution)
):
    food_list = institution.foods
    if not food_list:
        return HTTPException("404", detail="food not added")
    return food_list


@router.patch("/update/{food_id}")
async def update_food(food_update: FoodUpdate, food_id: str):
    food = await Food.find_one(Food.id == food_id)
    if not food:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food with id {food} not found",
        )

    food_data = encode_input(food_update)
    _ = await food.update({"$set": food_data})
    updated_food = await Food.find_one(Food.id == food_id)
    return updated_food


@router.patch("/{food_id}/set-image", response_model=FoodOut)
async def set_image_for_institution(food_id: str, file: UploadFile):
    food = await Food.find_one(Food.id == food_id)
    if food:
        await food.update({"$set": {Food.image: file.filename}})
    else:
        return HTTPException(status_code=404, detail="Object not found")
    async with aiofiles.open(file.filename, "wb") as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write

    new_food = await Food.find_one(Food.id == food_id)
    return new_food


@router.delete("/delete/{food_id}")
async def delete_food(food_id: str):
    food = await Food.find_one(Food.id == food_id)
    if not food:
        return HTTPException(
            status_code="404", detail=f"food with id {food_id} not exist"
        )
    await food.delete()
    return {"message": f"food with id {food.id} has deleted"}

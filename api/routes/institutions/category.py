"""Category router."""

from fastapi import APIRouter, Depends
from fastapi import APIRouter
from typing import List
from db.models import Category, Institution
from schemas.institutuions.category import Category as CategorySchema
from api.depends.institution.current_institution import current_institution

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("", response_model=CategorySchema)
async def create_category(
    category_data: CategorySchema,
):
    category = await Category(name=category_data.name,)
    await Category.create(category)
    return category


@router.get("", response_model=List[CategorySchema])
async def get_categories():
    categories = await Category.find_many()
    return categories


@router.delete("/{category_name}")
async def delete_category(
    category_name: str,
):
    categories = await Category.find_one(name=category_name)
    return categories

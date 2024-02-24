"""Category router."""

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi import APIRouter, HTTPException, status
from typing import List
from db.models import Category, Institution
from schemas.institutuions.category import Category as CategorySchema
from api.depends.institution import current_institution

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("/{institution_name}", response_model=CategorySchema)
async def create_category( 
                          category_data: CategorySchema,
                          institution: Institution = Depends(current_institution)
                          ):
    category = await Category(name=category_data.name, institution=institution)
    await Category.create(category)
    return category


@router.get("/{institution_name}", response_model=List[CategorySchema])
async def get_categories( 
                         institution: Institution = Depends(current_institution)
                         ):
    categories = await Category.find_many(institution=institution)
    return categories


@router.delete("/{institution_name}/{category_name}")
async def delete_category(
                          category_name: str,
                          institution: Institution = Depends(current_institution), ):
    categories = await Category.find_one(institution=institution, name=category_name)
    return categories

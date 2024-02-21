"""Food router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi import APIRouter, HTTPException, status
from typing import List
from db.models import Category, Institution
from schemas.institutuions.category import Category as CategorySchema

router = APIRouter(prefix="/category", tags=["Category"])





@router.post('/{institution_name}', response_model=CategorySchema)
async def create_category(
                        institution_name: str,
                        category_data: CategorySchema
                                ):
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    category = await Category(name=category_data.name, institution=institution)
    await Category.create(category)
    return category


@router.get('/{institution_name}', response_model=List[CategorySchema])
async def get_categories(institution_name: str):
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    categories = await Category.find_many(institution=institution)
    return categories
    
    
@router.delete('/{institution_name}/{category_name}')
async def delete_category(
                        institution_name: str,
                        category_name: str
                        ):
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    categories = await Category.find_one(institution=institution, name=category_name)
    return categories



"""Authentication router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from db.models import Tag as TagDoc
from schemas.institutuions.institutions import (
    InstitutionCreate,
    InstitutionOut,
    InstitutionDelete,
)
from typing import Optional, Annotated


router = APIRouter(prefix="/institutions", tags=["Institutions"])


@router.post("", response_model=InstitutionOut)
async def institution_create(
    institution_create: InstitutionCreate,
):
    user = await User.find_one(User.email == institution_create.user.email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    for i in institution_create.tags:
        if i not in await TagDoc.find_all().to_list():
            institution_create.tags.remove(i)
    institution = Institution(
        name=institution_create.name,
        description=institution_create.description,
        tags=institution_create.tags,
        owner=user,
    )
    await institution.insert()
    return institution


@router.get("")
async def institution_get():
    return await Institution.find_all().to_list()


@router.delete("")
async def institution_delete(institution_delete: InstitutionDelete):
    institution = await Institution.find_one(
        Institution.name == institution_delete.name
    )
    if institution is None:
        raise HTTPException(404, "No institution found with this name")
    await institution.delete()
    return {"message": f"Institution with name {institution.name} has been deleted "}

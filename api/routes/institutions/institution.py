"""Authentication router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from schemas.institutuions.institutions import InstitutionCreate
from typing import Optional, Annotated


router = APIRouter(prefix="/institutions", tags=["Institutions"])


@router.post('')
async def institution_create(
                            institution_create: InstitutionCreate,
    ):
    user = await User.find_one(User.email==institution_create.user.email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    institution = Institution(name=institution_create.name, 
                              description=institution_create.description,
                              owner=user
                                    )
    await institution.insert()
    return institution
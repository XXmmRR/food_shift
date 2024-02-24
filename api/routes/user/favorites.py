"""Adress router"""

from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from schemas.user.auth import AccessToken, RefreshToken
from db.models import User, Address
from core.jwt import (
    access_security,
    refresh_security,
    user_from_credentials,
    user_from_token,
)
from fastapi import Depends
from schemas.user.users import UserAuth
from db.models import Institution
from schemas.institutuions.institutions import InstitutionOut
from typing import List
from api.depends.user.current_user import current_user

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.post("", response_model=InstitutionOut)
async def favorite_create(
    favorite_institution: str,
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    institution = await Institution.find_one(
        Institution.InstitutionName == favorite_institution
    )
    if not user.favorites:
        user.favorites = []
    user.favorites.append(institution)
    await user.save()
    return institution


@router.get("", response_model=List[InstitutionOut])
async def get_favorites(
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    user = await user_from_credentials(auth)
    await user.fetch_all_links()
    return user.favorites


@router.delete("")
async def delete_favorites(
    favorite_institution: str,
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    user = await user_from_credentials(auth)
    await user.fetch_all_links()
    inst = await Institution.find_one(
        Institution.InstitutionName == favorite_institution
    )
    for i in user.favorites:
        if i.InstitutionName == inst.InstitutionName:
            user.favorites.remove(i)
            return {
                "message": f"institution with id {inst.id} has been removed from favorites"
            }
    return HTTPException(
        status_code=404,
        detail=f"favorite institution with {inst.InstitutionName} does not exits",
    )

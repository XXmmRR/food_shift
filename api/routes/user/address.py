"""Adress router"""

from fastapi import APIRouter, HTTPException, Security, Depends
from fastapi_jwt import JwtAuthorizationCredentials

from db.models import User, Address
from core.jwt import (
    access_security,
    user_from_credentials,
)
from schemas.user.address import AddressCreate, AddressOut
from schemas.institutuions.food import PyObjectId
from typing import List
from api.depends.user.current_user import current_user


router = APIRouter(prefix="/address", tags=["Address"])


@router.post("", response_model=AddressCreate)
async def create_address(
    address: AddressCreate,
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    address = Address(
        lat=address.lat,
        lon=address.lon,
        name=address.name,
        orient=address.orient,
        user=user,
    )
    await address.insert()
    return address


@router.get("", response_model=List[AddressOut])
async def get_address(
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    if not user.addresses:
        raise HTTPException(status_code=404, detail="user don't have address")
    return user.addresses


@router.delete("/{id}")
async def delete_address(
    id: PyObjectId,
    auth: JwtAuthorizationCredentials = Security(access_security),
    user: User = Depends(current_user),
):
    user = await user_from_credentials(auth)
    address = await Address.get(id)
    if not address:
        raise HTTPException(status_code=404, detail="address not found")
    await address.delete()
    return {"message": f"address has been deleted"}

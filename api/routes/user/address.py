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
from schemas.user.users import UserAuth
from utils.password import hash_password
from schemas.user.address import AddressCreate, AddressOut
from schemas.institutuions.food import PyObjectId
from typing import List


router = APIRouter(prefix="/address", tags=["Address"])


@router.post("", response_model=AddressCreate)
async def create_address(
    address: AddressCreate,
    auth: JwtAuthorizationCredentials = Security(access_security),
):
    user = await user_from_credentials(auth)
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
async def get_address(auth: JwtAuthorizationCredentials = Security(access_security)):
    user = await user_from_credentials(auth)
    if not user.addresses:
        raise HTTPException(status_code=404, detail="user don't have address")
    return user.addresses


@router.delete("/{id}")
async def delete_address(id: PyObjectId,
                        auth: JwtAuthorizationCredentials = Security(access_security)):
    user = await user_from_credentials(auth)
    address = await Address.get(id)
    if not address:
        raise HTTPException(status_code=404, detail='address not found')
    await address.delete()
    return {"message": f"address has been deleted"}


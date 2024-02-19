"""Adress router"""


from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from schemas.user.auth import AccessToken, RefreshToken
from db.models import User, Address
from core.jwt import access_security, refresh_security, user_from_credentials, user_from_token
from schemas.user.users import UserAuth
from utils.password import hash_password
from schemas.user.address import AddressCreate
from typing import List

router = APIRouter(prefix="/address", tags=["Address"])


@router.post('', response_model=AddressCreate)
async def create_address(
                        address: AddressCreate,
                        auth: JwtAuthorizationCredentials = Security(access_security),
                         ):
    user = await user_from_credentials(auth)
    address =  Address(lat=Address.lat,
                            lon=Address.lon,
                            name=Address.name,
                            orient=Address.orient,
                            user=user
                            )
    await address.insert()
    return address


@router.get('', response_model=List[AddressCreate])
async def get_address(auth: JwtAuthorizationCredentials = Security(access_security)):
    user = await user_from_credentials(auth)
    addresses = await Address.find_all(Address.user==user)
    if not addresses:
        return HTTPException(status_code=404, detail="User don't have address")
    return addresses
    

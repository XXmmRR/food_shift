"""Adress router"""


from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from schemas.user.auth import AccessToken, RefreshToken
from db.models import User, Address
from core.jwt import access_security, refresh_security, user_from_credentials, user_from_token
from schemas.user.users import UserAuth
from utils.password import hash_password
from schemas.user.address import AddressCreate, AddressOut
from typing import List


router = APIRouter(prefix="/address", tags=["Address"])


@router.post('', response_model=AddressCreate)
async def create_address(
                        address: AddressCreate,
                        auth: JwtAuthorizationCredentials = Security(access_security),
                         ):
    user = await user_from_credentials(auth)
    address =  Address(lat=address.lat,
                        lon=address.lon,
                        name=address.name,
                        orient=address.orient,
                        user=user
                            )
    await address.insert()
    return address


@router.get('', response_model=List[AddressOut])
async def get_address(auth: JwtAuthorizationCredentials = Security(access_security)):
    user = await user_from_credentials(auth)
    address = await Address.find_many(Address.user.id == user.id).to_list()
    return [AddressOut(lat=x.lat, lon=x.lon, orient=x.orient, name=x.name, id=str(x.id)) for x in address]


@router.delete('/{id}')
async def delete_address(auth: JwtAuthorizationCredentials = Security(access_security)):
    user = await user_from_credentials(auth)
    address = await Address.find_one(Address.id==id, Address.user.id==user.id)
    await address.delete()
    return {'message': f'address with {str(address.id)} has been deleted'}
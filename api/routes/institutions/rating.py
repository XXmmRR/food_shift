"""Rating router."""

from fastapi import APIRouter, HTTPException, UploadFile, File, Security
from db.models import Institution, User
from schemas.user.users import UserAuth
from fastapi import APIRouter, HTTPException, status
from db.models import Tag as TagDoc
from typing import List
from schemas.institutuions.ratings import RatingSchema
from db.models import Food, Institution, Rating
from utils.pydantic_encoder import encode_input
import aiofiles
from fastapi_jwt import JwtAuthorizationCredentials

from schemas.user.auth import AccessToken, RefreshToken
from db.models import User, Address
from core.jwt import (
    access_security,
    user_from_token,
)



router = APIRouter(prefix="/rating", tags=["Rating"])


@router.post('/{institution_name}', response_model=RatingSchema)
async def create_rating(institution_name: str,
                        rating_data: RatingSchema,
                        auth: JwtAuthorizationCredentials = Security(access_security),
                        ):
    user = await user_from_token(auth) 
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    rating = Rating(user=user, institution=institution, stars=rating_data.stars)
    await Rating.create(rating)
    return rating


@router.get('/{institution_name}', response_model=List[RatingSchema])
async def get_ratings(institution_name: str):
    institution = await Institution.find_one(Institution.InstitutionName==institution_name)
    return institution.ratings

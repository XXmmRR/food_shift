"""Rating router."""

from fastapi import APIRouter, Depends, Security
from db.models import Institution, User
from schemas.user.users import UserAuth
from typing import List
from schemas.institutuions.ratings import RatingSchema
from db.models import Food, Institution, Rating
from utils.pydantic_encoder import encode_input
import aiofiles
from fastapi_jwt import JwtAuthorizationCredentials
from api.depends.institution.current_institution import current_institution
from api.depends.user.current_user import current_user
from schemas.user.auth import AccessToken, RefreshToken
from db.models import User, Address
from core.jwt import access_security, user_from_token, user_from_credentials


router = APIRouter(prefix="/rating", tags=["Rating"])


@router.post("/{institution_name}", response_model=RatingSchema)
async def create_rating(
    rating_data: RatingSchema,
    auth: JwtAuthorizationCredentials = Security(access_security),
    institution: Institution = Depends(current_institution),
    user: User = Depends(current_user),
):
    rating = Rating(user=user, institution=institution, stars=rating_data.stars)
    await Rating.create(rating)
    return rating


@router.get("/{institution_name}", response_model=List[RatingSchema])
async def get_ratings(
    institution: Institution = Depends(current_institution),
):
    return institution.ratings

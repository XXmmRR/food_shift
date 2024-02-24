"""Rating router."""

from fastapi import APIRouter, Depends, Security
from db.models import Institution, User
from typing import List
from schemas.institutuions.ratings import RatingSchema
from db.models import Institution, Rating
from fastapi_jwt import JwtAuthorizationCredentials
from api.depends.institution.current_institution import current_institution
from api.depends.user.current_user import current_user
from db.models import User
from core.jwt import access_security


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

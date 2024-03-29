"""Authentication router."""

from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from schemas.user.auth import AccessToken, RefreshToken
from db.models import User
from core.jwt import access_security, refresh_security
from schemas.user.users import UserAuth
from utils.password import hash_password


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(user_auth: UserAuth) -> RefreshToken:
    """Authenticate and returns the user's JWT."""
    user = await User.find_one(User.email == user_auth.email)
    if user is None or hash_password(user_auth.password) != user.password:
        raise HTTPException(status_code=401, detail="Bad email or password")
    if user.email_confirmed_at is None:
        raise HTTPException(status_code=400, detail="Email is not yet verified")
    access_token = access_security.create_access_token({"username": user.email})
    refresh_token = refresh_security.create_refresh_token({"username": user.email})
    return RefreshToken(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh")
async def refresh(
    auth: JwtAuthorizationCredentials = Security(refresh_security),
) -> AccessToken:
    """Return a new access token from a refresh token."""
    access_token = access_security.create_access_token(subject=auth.subject)
    return AccessToken(access_token=access_token)

"""Registration router."""

from fastapi import APIRouter, Body, HTTPException, Response
from pydantic import EmailStr

from db.models import User
from schemas.user.users import UserOut, UserRegister
from core.jwt import access_security, user_from_token
from utils.mail import send_password_reset_email
from utils.password import hash_password

router = APIRouter(prefix="/register", tags=["Register"])

embed = Body(..., embed=True)


@router.post("", response_model=UserOut)
async def user_registration(user_auth: UserRegister):
    """Create a new user."""
    user = await User.find_one(User.email == user_auth.email)
    if user is not None:
        raise HTTPException(409, "User with that email already exists")
    hashed = hash_password(user_auth.password)
    user = User(
        first_name=user_auth.first_name,
        last_name=user_auth.last_name,
        phone=user_auth.phone,
        email=user_auth.email,
        password=hashed,
    )
    await user.create()
    return user


@router.post("/forgot-password")
async def forgot_password(email: EmailStr = embed) -> Response:
    """Send password reset email."""
    user = await User.find_one(User.email == email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is not None:
        raise HTTPException(400, "Email is already verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    token = access_security.create_access_token({"username": user.email})
    await send_password_reset_email(email, token)
    return Response(status_code=200)


@router.post("/reset-password/{token}", response_model=UserOut)
async def reset_password(token: str, password: str = embed):  # type: ignore[no-untyped-def]
    """Reset user password from token value."""
    user = await user_from_token(token)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    if user.email_confirmed_at is None:
        raise HTTPException(400, "Email is not yet verified")
    if user.disabled:
        raise HTTPException(400, "Your account is disabled")
    user.password = hash_password(password)
    await user.save()
    return user

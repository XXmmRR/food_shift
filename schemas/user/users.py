"""User models."""

from datetime import datetime
from typing import Annotated, Any, Optional

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegister(BaseModel):
    """User register."""

    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str


class UserAuth(BaseModel):
    """User login"""

    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """Updatable user fields."""

    email: EmailStr | None = None

    # User information
    first_name: str | None = None
    last_name: str | None = None


class UserOut(UserUpdate):
    """User fields returned to the client."""

    email: Annotated[str, Indexed(EmailStr, unique=True)]
    disabled: Optional[bool] = None


class UserMail(BaseModel):
    """User email for links"""

    email: Annotated[str, Indexed(EmailStr, unique=True)]

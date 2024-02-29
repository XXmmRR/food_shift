from pydantic import BaseModel, Field
from schemas.user.users import UserMail
from typing import Optional, List
from schemas.institutuions.tags import Tag


class InstitutionCreate(BaseModel):
    InstitutionName: str = Field(min_length=2, max_length=30)
    description: str = Field(min_length=20, max_length=500)
    user: UserMail
    tags: Optional[List[Tag]] = None


class InstitutionOut(BaseModel):
    InstitutionName: str = Field(min_length=2, max_length=30)
    image: Optional[str] = None
    description: str = Field(min_length=20, max_length=500)
    tags: Optional[List[Tag]] = None


class InstitutionUpdate(BaseModel):
    InstitutionName: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None

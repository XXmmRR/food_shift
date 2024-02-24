from pydantic import BaseModel
from schemas.user.users import UserMail
from typing import Optional, List
from schemas.institutuions.tags import Tag


class InstitutionCreate(BaseModel):
    InstitutionName: str
    description: str
    user: UserMail
    tags: Optional[List[Tag]] = None


class InstitutionOut(BaseModel):
    InstitutionName: str
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class InstitutionUpdate(BaseModel):
    InstitutionName: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None

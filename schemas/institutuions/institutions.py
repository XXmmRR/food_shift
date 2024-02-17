from pydantic import BaseModel
from schemas.user.users import UserMail
from fastapi import UploadFile, File
from typing import Optional, List
from schemas.institutuions.tags import Tag


class InstitutionCreate(BaseModel):
    name: str
    description: str
    user: UserMail
    tags: Optional[List[Tag]] = None


class InstitutionOut(BaseModel):
    name: str
    image: Optional[str] = None
    tags: Optional[List[Tag]] = None


class InstitutionDelete(BaseModel):
    name: str

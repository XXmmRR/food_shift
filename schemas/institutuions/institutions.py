from pydantic import BaseModel
from schemas.user.users import UserMail
from fastapi import UploadFile, File
from typing import Optional

class InstitutionCreate(BaseModel):
    name: str
    description: str
    user: UserMail


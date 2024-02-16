from pydantic import BaseModel
from schemas.user.users import UserMail
from fastapi import UploadFile, File
from typing import Optional

class InstitutionCreate(BaseModel):
    name: str
    description: str
    user: UserMail


class InstitutionOut(BaseModel):
    name: str
    image: Optional[str] = None
    description: str        
    
    
class InstitutionDelete(BaseModel):
    name: str
    
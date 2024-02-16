"""Authentication router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from schemas.institutuions.institutions import InstitutionCreate, InstitutionOut
from typing import Optional, Annotated


router = APIRouter(prefix="/tags", tags=["Tags"])


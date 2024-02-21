"""Food router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from fastapi import APIRouter, HTTPException, status
from db.models import Tag as TagDoc
from typing import List
from pymongo.errors import DuplicateKeyError
from schemas.institutuions.institutions import (
    InstitutionCreate,
    InstitutionOut,
    InstitutionUpdate
)
from utils.pydantic_encoder import encode_input
import aiofiles



router = APIRouter(prefix="/food", tags=["Food"])



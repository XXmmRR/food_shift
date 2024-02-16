"""Authentication router."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from db.models import Institution, User
from schemas.user.users import UserAuth
from schemas.institutuions.tags import Tag
from typing import Optional, Annotated
from db.models import Tag as TagDoc

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post('', response_model=Tag)
async def create_tag(tag_create: Tag):
    tag = TagDoc(tag_name=tag_create.tag_name,
                 draft=tag_create.draft
                 )
    await TagDoc.create(tag)
    return tag

"""Authentication router."""

from fastapi import APIRouter
from schemas.institutuions.tags import Tag, TagDelete
from typing import List
from db.models import Tag as TagDoc

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("", response_model=Tag)
async def create_tag(tag_create: Tag):
    tag = TagDoc(tag_name=tag_create.tag_name, draft=tag_create.draft)
    await TagDoc.create(tag)
    return tag


@router.get("", response_model=List[Tag])
async def tag_list():
    return await TagDoc.find_all().to_list()


@router.delete("")
async def delete_tag(tag_delete: TagDelete):
    tag = await TagDoc.find_one(TagDoc.tag_name == tag_delete.tag_name)
    await tag.delete()
    return {"message": f"tag with name {tag.tag_name} has deleted"}

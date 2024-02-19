"""Authentication router."""

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



router = APIRouter(prefix="/institutions", tags=["Institutions"])


@router.post("", response_model=InstitutionOut)
async def institution_create(
    institution_create: InstitutionCreate,
):
    user = await User.find_one(User.email == institution_create.user.email)
    if user is None:
        raise HTTPException(404, "No user found with that email")
    for i in institution_create.tags:
        if i not in await TagDoc.find_all().to_list():
            institution_create.tags.remove(i)
    try:
        institution = Institution(
            InstitutionName=institution_create.InstitutionName,
            description=institution_create.description,
            tags=institution_create.tags,
            owner=user,
        )
        await institution.insert()
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail='Name alredy exist')
    return institution


@router.patch("/{name}/set-image")
async def set_image_for_institution(name: str, file: UploadFile):
    institution = await Institution.find_one(Institution.InstitutionName==name)
    if institution:
        institution.update({"$set": {Institution.image: file.filename}})
    else:
        return HTTPException(status_code=404, detail='Object not found')
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write

    new_institution = await Institution.find_one(Institution.InstitutionName==name)
    return new_institution


@router.get("", response_model=List[InstitutionOut])
async def institution_get():
    inst =  await Institution.find_all().to_list()
    return inst


@router.patch('/{name}', response_model=InstitutionOut)
async def institution_update(name: str, institution_update: InstitutionUpdate):
    institution = await Institution.find_one(Institution.InstitutionName==name)
    if not institution:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )
    institution_data = encode_input(institution_update)
    _ = await institution.update({"$set": institution_data})
    updated_institution = await Institution.find_one(Institution.InstitutionName==name)
    return updated_institution



@router.delete("/{name}")
async def institution_delete(name):
    institution = await Institution.find_one(
        Institution.name == name
    )
    if institution is None:
        raise HTTPException(404, "No institution found with this name")
    await institution.delete()
    return {"message": f"Institution with name {institution.name} has been deleted "}

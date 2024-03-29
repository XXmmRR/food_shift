from fastapi import APIRouter, Depends, Security
from db.models import Ingridients
from schemas.institutuions.ingridient import Ingridient
from typing import List
from schemas.institutuions.food import PyObjectId

router = APIRouter(prefix='/ingridients')


@router.get('', response_model=List[Ingridient])
async def get_ingridients():
    return await Ingridients.find_all()

@router.post('', response_model=Ingridient)
async def create_ingridient(ingridient_data: Ingridient):
    ingridient = Ingridients(**ingridient_data)
    await ingridient.save()
    return ingridient

@router.delete('/{id}')
async def delete_ingridient(id: PyObjectId):
    ingridient = await Ingridients.find_one(Ingridient.id == id)
    await ingridient.delete()
    return {"message": f"ingridient with id {str(id)} has deleted"}
 
    
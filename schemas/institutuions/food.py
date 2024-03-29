from pydantic import BaseModel, Field
from typing import Optional, Any
from bson import ObjectId

from bson import ObjectId
from pydantic_core import core_schema
from schemas.institutuions.category import Category
from typing import List
from schemas.institutuions.institutions import InstitutionOut

class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(cls.validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)


class FoodModel(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    description: str = Field(min_length=1, max_length=255)
    price: int = Field(ge=1)
    draft: bool
    category: Category

class FoodeCreate(FoodModel):
    active: bool
    
    
class FoodOut(FoodModel):
    id: PyObjectId
    category: Category
    image: Optional[str] = None


class FoodList(BaseModel):
    food_list: List[FoodOut]
    institution: InstitutionOut
    


class FoodUpdate(FoodeCreate):
    pass

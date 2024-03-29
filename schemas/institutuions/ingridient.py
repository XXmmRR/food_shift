from pydantic import BaseModel, Field


class Ingridient(BaseModel):
    name: str = Field(min_length=1, max_length=25)
    photo: str

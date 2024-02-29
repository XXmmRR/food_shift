from pydantic import BaseModel, Field


class Tag(BaseModel):
    tag_name: str = Field(min_length=3, max_length=30)
    draft: bool


class TagDelete(BaseModel):
    tag_name: str

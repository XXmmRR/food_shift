from pydantic import BaseModel


class Tag(BaseModel):
    tag_name: str
    draft: bool


class TagDelete(BaseModel):
    tag_name: str

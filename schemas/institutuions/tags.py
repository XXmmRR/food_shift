from pydantic import BaseModel


class Tag(BaseModel):
    TagName: str
    draft: bool


class TagDelete(BaseModel):
    tag_name: str

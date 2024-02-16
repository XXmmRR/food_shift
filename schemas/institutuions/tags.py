from pydantic import BaseModel

class Tag(BaseModel):
    tag_name: str
    draft: bool
    
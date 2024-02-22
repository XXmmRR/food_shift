from pydantic import BaseModel, Field

class RatingSchema(BaseModel):
    stars: float = Field(le=5)
    
    
from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3)
    completed: bool = False
from pydantic import BaseModel, Field
from typing import Literal

class createTask(BaseModel):
    title:str = Field(min_length=1, max_length=100, strip_whitespace=True)
    description:str = Field(min_length=1, max_length=500, strip_whitespace=True)
    priority : Literal["Low","Medium", "High"]

class updateTask(BaseModel):
    title:str = Field(min_length=1, max_length=100, strip_whitespace=True)
    description:str = Field(min_length=1, max_length=500, strip_whitespace=True)
    priority : Literal["Low","Medium", "High"]

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    completed: bool

    class Config:
        from_attributes = True
from pydantic import BaseModel

class createTask(BaseModel):
    title:str
    description:str
    priority:str

class updateTask(BaseModel):
    title:str
    description:str
    priority:str
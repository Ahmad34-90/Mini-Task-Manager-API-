from pydantic import BaseModel

class createTask(BaseModel):
    title:str
    description:str
    priority:str

class updateTask(BaseModel):
    title:str
    description:str
    priority:str

class TaskResponse(BaseModel):
    id:str
    title:str
    dscription:str
    priority:str
    complete:bool

    class config:
        from_attributes = True
from fastapi import FastAPI
from app.model import Task
from app.database import Base, engine
from app.schemas import createTask, updateTask

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Task Manager API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)

tasks= []

@app.get("/")
def root():
    return {
        "message": "Mini Task Manager API is running."
    }

@app.post("/tasks")
def create_task(task: createTask):
    task_id = len(task)+1

    new_task={
        "id":task_id,
        "title":task.title,
        "dscription":task.description,
        "priority":task.priority
    }

    tasks.append(new_task)

    return {
        "message":"Task create successfully",
        "task":new_task
    }

@app.get("/tasks/{task_id}")
def get_tasks(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return{
        "message":"task not found"
    }

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
        return{
            "message":"Task deleted successfully"
        }
    return{
        "message":"Task not found"
    }

@app.put("/tasks/{task_id}")
def update_task(task_id:int, task_update:updateTask):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["description"] = task_update.description
            task["priority"] = task_update.priority
        return{
            "message":"Task update Successfully",
            "task":task
        }
    return{
        "message":"task not found"
    }

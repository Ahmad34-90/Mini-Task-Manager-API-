from fastapi import FastAPI, Depends, HTTPException
from app.model import Task
from app.database import Base, engine, get_db
from app.schemas import createTask, updateTask, TaskResponse
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Task Manager API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)



@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return {
        "tasks": tasks
    }

@app.post("/tasks")
def create_task(task: createTask, db:Session = Depends(get_db)):

    new_task= Task(
       title= task.title,
       description = task.description,
       priority= task.priority
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message":"Task create successfully",
        "task":new_task
    }

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_tasks(task_id:int, db:Session = Depends(get_db)):
    task= db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task 

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int, db:Session= Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
    
    db.delete(task)
    db.commit()

    return {
        "message":"Task deleted Completely"
    }

@app.put("/tasks/{task_id}")
def update_task(task_id:int, task_update:updateTask, db:Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
    
    task.title = task_update.title
    task.description = task_update.description
    task.priority = task_update.priority

    db.commit()
    db.refresh(task)

    return{
        "message":"Task Updated Succesfully",
        "task":task
    }

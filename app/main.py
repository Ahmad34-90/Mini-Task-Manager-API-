from fastapi import FastAPI
from app.schemas import createTask
app = FastAPI(
    title="Mini Task Manager API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Mini Task Manager API is running."
    }

@app.post("/tasks")
def create_task(task: createTask):
    return {
        "message":"Task create successfully",
        "task":task
    }
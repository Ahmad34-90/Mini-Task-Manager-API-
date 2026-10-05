from fastapi import FastAPI

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
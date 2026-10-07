from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Mini Task Manager API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)


app.include_router(tasks.router)
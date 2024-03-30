from fastapi import FastAPI
from .config.database import engine
from .routers import users
from . import models

app = FastAPI()

app.include_router(users.router)

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"message": "hey hey hey yo"}
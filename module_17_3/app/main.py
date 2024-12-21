from fastapi import FastAPI
from Module_17.module_17_3.app.models import user, task

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
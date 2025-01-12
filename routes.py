from fastapi import APIRouter, HTTPException
from model import Task

router = APIRouter()
tasks= {}

@router.get("/get_tasks/")
def get_tasks():
    return {"Message": "All the tasks","Tasks": tasks}

@router.post("/set_tasks/")
def set_tasks(task: Task):
    if tasks.get(task.taskid) is not None:
        raise HTTPException(status_code=400, detail="Task already Exists")
    tasks.update(task)
    return {"Message": "Task Created successfuly", "Tasks":tasks}
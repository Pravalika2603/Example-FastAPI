from fastapi import APIRouter, HTTPException
from model import Task

router = APIRouter()
tasks= []

@router.get("/get_tasks/")
def get_tasks():
    return {"Message": "All the tasks","Tasks": tasks}

@router.post("/set_tasks/")
def set_tasks(task: Task):
    taskids = [task.taskid for task in tasks]
    if task.taskid in taskids:
        raise HTTPException(status_code=400, detail="Task already Exists")
    tasks.append(task)
    return {"Message": "Task Created successfuly", "Tasks":tasks}

@router.get("/get_task/{taskid}")
def get_task(taskid):
    for task in tasks:
        if task.taskid == int(taskid):
            return {"Message": "Task Found", "Task":task}
    raise HTTPException(status_code=404, detail="Task Not Found")
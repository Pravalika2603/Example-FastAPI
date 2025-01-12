import datetime
from pydantic import BaseModel

class Task(BaseModel):
    taskid: int
    taskname: str
    description: str = None
    time: datetime.datetime
    status: str = "pending"
    
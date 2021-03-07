from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TaskStatus(str, Enum):
    created = 'created'
    opened = 'opened'
    completed = 'completed'


class BaseTask(BaseModel):
    title: str
    description: str
    status: TaskStatus
    user_id: Optional[str]


class Task(BaseTask):
    id: str
    created: datetime
    updated: datetime


class TaskIn(BaseTask):
    pass


class TasksList(BaseModel):
    results: List[Task]

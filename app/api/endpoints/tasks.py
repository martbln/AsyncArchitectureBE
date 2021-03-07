import uuid
from datetime import datetime

from fastapi import APIRouter, Depends

import pytz

from app.core.consts import DATETIME_FORMAT
from app.models.tasks import Task, TasksList
from app.utils import get_db

router = APIRouter()


@router.get('/', response_model=TasksList)
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.get('tasks')
    return {'results': [Task(**user) for user in tasks]}


@router.get('/{task_id}', response_model=Task)
async def get_task_by_id(task_id: str, db: Session = Depends(get_db)):
    task = db.get(task_id)
    if task:
        return Task(**task)
    return None


@router.post('/', response_model=Task)
async def create_task(task: Task, db: Session = Depends(get_db)):
    task_data = {
        **task.dict(),
        'created': datetime.now(tz=pytz.UTC).strftime(DATETIME_FORMAT),
        'updated': datetime.now(tz=pytz.UTC).strftime(DATETIME_FORMAT),
        'id': str(uuid.uuid4())
    }
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return Task(**task_data)


@router.post('/{task_id}&{user_id}', response_model=Task)
async def set_task_to_user(
        task_id: str, user_id: str, db: Session = Depends(get_db)):
    task = db.get(task_id)
    task['user_id'] = user_id
    db.update(task)
    db.refresh(task)
    return Task(**task)


@router.post('/{task_id}', response_model=Task)
async def complete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.get(task_id)
    task['status'] = 'completed'
    db.update(task)
    db.refresh(task)
    return Task(**task)

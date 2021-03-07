from fastapi import APIRouter, Depends

from app.models.users import User, UsersList
from app.utils import get_db

router = APIRouter()


@router.get('/', response_model=UsersList)
async def get_users(db: Session = Depends(get_db)):
    users = db.get('users')
    return {'results': [User(**user) for user in users]}


@router.get('/{user_id}', response_model=User)
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    user = db.get(user_id)
    if user:
        return User(**user)
    return None

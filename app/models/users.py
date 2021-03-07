from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class UserRole(str, Enum):
    popug = 'popug'
    admin = 'admin'
    manager = 'manager'


class BaseUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    role: UserRole


class User(BaseUser):
    id: str
    created: datetime
    updated: datetime


class UserIn(BaseUser):
    pass


class UsersList(BaseModel):
    results: List[User]

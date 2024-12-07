"""
Маршруты для работы с пользователями.

Содержит примеры работы с объектами `User`.
"""

from fastapi import APIRouter
from typing import List
from models.user import User
from db.database import users_db

router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users():
    """
    Возвращает список всех пользователей.

    Returns:
        List[User]: Список пользователей.
    """
    return users_db


@router.get("/users/{id}", response_model=User)
def get_user(id: int):
    """
    Возвращает пользователя по ID.

    Args:
        id (int): ID пользователя.

    Returns:
        User: Объект пользователя.
    """
    for user in users_db:
        if user.id == id:
            return user
    return {"error": "User not found"}

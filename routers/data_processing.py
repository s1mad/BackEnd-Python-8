"""
Маршруты для обработки данных запросов.

Содержит примеры обработки данных формы и JSON.
"""

from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter()


class RegisterData(BaseModel):
    """
    Модель данных для регистрации.

    Attributes:
        username (str): Имя пользователя.
        email (str): Электронная почта.
        password (str): Пароль.
    """
    username: str
    email: str
    password: str


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    """
    Обрабатывает данные формы для входа.

    Args:
        username (str): Имя пользователя.
        password (str): Пароль.

    Returns:
        dict: Словарь с приветствием пользователя.
    """
    return {"message": f"Welcome, {username}!"}


@router.post("/register")
def register(data: RegisterData):
    """
    Обрабатывает JSON-данные для регистрации.

    Args:
        data (RegisterData): Данные для регистрации.

    Returns:
        dict: Словарь с сообщением о успешной регистрации.
    """
    return {"message": f"User {data.username} registered successfully!"}

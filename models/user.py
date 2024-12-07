"""
Модель данных пользователя.
"""

from pydantic import BaseModel


class User(BaseModel):
    """
    Модель данных пользователя.

    Attributes:
        id (int): Уникальный идентификатор пользователя.
        username (str): Имя пользователя.
        email (str): Электронная почта пользователя.
        password (str): Пароль пользователя.
    """
    id: int
    username: str
    email: str
    password: str

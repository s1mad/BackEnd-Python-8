"""
Маршруты для базовых операций.

Содержит базовый маршрут "/" для проверки работы приложения.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    """
    Возвращает приветственное сообщение.

    Returns:
        dict: Словарь с приветственным сообщением.
    """
    return {"message": "Hello, World!"}

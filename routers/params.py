"""
Маршруты для работы с параметрами пути и строки запроса.

Содержит примеры использования параметров `path` и `query`.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/greet/{name}")
def greet(name: str):
    """
    Возвращает приветствие с именем.

    Args:
        name (str): Имя пользователя.

    Returns:
        dict: Словарь с приветствием.
    """
    return {"message": f"Hello, {name}!"}


@router.get("/search")
def search(query: str):
    """
    Возвращает сообщение с поисковым запросом.

    Args:
        query (str): Поисковый запрос.

    Returns:
        dict: Словарь с результатом поиска.
    """
    return {"message": f"You searched for: {query}"}

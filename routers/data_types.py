"""
Маршруты для работы с различными типами данных и ответов.

Содержит примеры отправки JSON, файлов и перенаправлений.
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

router = APIRouter()


@router.get("/json")
def get_json():
    """
    Возвращает JSON-объект с данными о пользователе.

    Returns:
        dict: JSON-объект с данными.
    """
    return {"name": "Your Name", "age": 20, "hobby": "coding"}


@router.get("/file")
def get_file():
    """
    Создает и возвращает текстовый файл.

    Returns:
        FileResponse: Текстовый файл с произвольным содержимым.
    """
    with open("example.txt", "w") as f:
        f.write("This is an example file.")
    return FileResponse("example.txt", media_type="text/plain")


@router.get("/redirect")
def redirect_to_root():
    """
    Выполняет перенаправление на корневой маршрут.

    Returns:
        RedirectResponse: Ответ с перенаправлением.
    """
    return RedirectResponse("/")

"""
Маршруты для работы с заголовками и куками.

Содержит примеры чтения заголовков и установки/чтения кук.
"""

from fastapi import APIRouter, Header, Cookie, Response

router = APIRouter()


@router.get("/headers")
def get_headers(headers: dict = Header(None)):
    """
    Возвращает все заголовки запроса.

    Args:
        headers (dict): Заголовки запроса.

    Returns:
        dict: Словарь с заголовками.
    """
    return {"headers": headers}


@router.get("/set-cookie")
def set_cookie(response: Response):
    """
    Устанавливает куку с именем `username` и значением `your_name`.

    Args:
        response (Response): Объект ответа.

    Returns:
        dict: Словарь с сообщением об успешной установке куки.
    """
    response.set_cookie(key="username", value="your_name")
    return {"message": "Cookie set successfully!"}


@router.get("/get-cookie")
def get_cookie(username: str = Cookie(None)):
    """
    Возвращает значение куки `username`.

    Args:
        username (str): Значение куки `username`.

    Returns:
        dict: Словарь с именем пользователя.
    """
    return {"username": username}

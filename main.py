"""
Этот файл инициализирует приложение FastAPI и подключает все модули маршрутов.
"""

from fastapi import FastAPI
from routers import base, params, data_types, headers_and_cookies, data_processing, users

app = FastAPI(title="FastAPI Project")

# Подключение маршрутов
app.include_router(base.router, tags=["Base"])
app.include_router(params.router, tags=["Path and Query Parameters"])
app.include_router(data_types.router, tags=["Data Types and Responses"])
app.include_router(headers_and_cookies.router, tags=["Headers and Cookies"])
app.include_router(data_processing.router, tags=["Data Processing"])
app.include_router(users.router, tags=["Users"])

"""
Файл с мок-данными для базы данных пользователей.
"""

from models.user import User

users_db = [
    User(id=1, username="user1", email="user1@example.com", password="pass1"),
    User(id=2, username="user2", email="user2@example.com", password="pass2")
]

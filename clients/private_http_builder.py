from typing import TypedDict

from httpx import Client
from clients.authentification.authentification_client import get_authentification_client, LoginRequestDict


class AuthentificationUserDict(TypedDict):  # Структура данных пользователя для авторизации
    email: str
    password: str


# Создаем private builder
def get_private_http_client(user: AuthentificationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentification_client = get_authentification_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )

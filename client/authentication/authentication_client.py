from httpx import Response
from client.users.api_client import APIClient
from typing import TypedDict

class loginReq(APIClient):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
        Клиент для работы с /api/v1/authentication
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self,request: dict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/authentication/login", json=request)

    def refresh_token_api(self,request):
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/authentication/refresh", json=request)


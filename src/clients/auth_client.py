from requests import Response

from src.clients.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, username: str, password: str) -> Response:
        payload = {
            "username": username,
            "password": password,
            "expiresInMins": 30,
        }
        return self.post("/auth/login", json=payload)
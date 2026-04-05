from typing import Any

import requests

from src.utils.exceptions import ApiClientError
from src.utils.helpers import build_headers
from src.utils.logger import get_logger


logger = get_logger(__name__)


class BaseClient:
    def __init__(self, base_url: str, token: str | None = None, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _request(
        self,
        method: str,
        endpoint: str,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> requests.Response:
        url = self._build_url(endpoint)
        headers = build_headers(self.token)

        logger.info("Sending %s request to %s", method.upper(), url)

        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                json=json,
                params=params,
                headers=headers,
                timeout=self.timeout,
            )
        except requests.RequestException as exc:
            logger.exception("Request failed: %s %s", method.upper(), url)
            raise ApiClientError(f"Request failed for {method.upper()} {url}: {exc}") from exc

        logger.info("Received response: %s for %s %s", response.status_code, method.upper(), url)
        return response

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> requests.Response:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json: dict[str, Any] | None = None) -> requests.Response:
        return self._request("POST", endpoint, json=json)

    def put(self, endpoint: str, json: dict[str, Any] | None = None) -> requests.Response:
        return self._request("PUT", endpoint, json=json)

    def delete(self, endpoint: str) -> requests.Response:
        return self._request("DELETE", endpoint)
import pytest

from src.schemas.auth_schema import LOGIN_RESPONSE_SCHEMA
from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.smoke
def test_user_can_login_successfully(auth_client):
    response = auth_client.login(
        username="emilys",
        password="emilyspass",
    )

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()
    ResponseValidator.validate_schema(response_data, LOGIN_RESPONSE_SCHEMA)

    assert response_data["accessToken"]
    assert response_data["refreshToken"]
    assert response_data["username"] == "emilys"
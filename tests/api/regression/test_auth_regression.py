import pytest

from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.regression
def test_login_with_invalid_credentials_returns_400(auth_client):
    response = auth_client.login(
        username="invalid_user",
        password="invalid_pass",
    )

    ResponseValidator.validate_status_code(response.status_code, 400)

    response_data = response.json()
    assert "message" in response_data
import pytest

from src.schemas.cart_schema import CART_SCHEMA
from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_cart_returns_valid_cart(cart_client):
    response = cart_client.get_single_cart(1)

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()
    ResponseValidator.validate_schema(response_data, CART_SCHEMA)

    assert response_data["id"] == 1


@pytest.mark.api
@pytest.mark.smoke
def test_create_cart_returns_200_or_201(cart_client):
    payload_products = [
        {
            "productId": 1,
            "quantity": 2
        }
    ]

    response = cart_client.create_cart(
        user_id=5,
        date="2026-04-05",
        products=payload_products,
    )

    assert response.status_code in [200, 201]

    response_data = response.json()
    assert response_data["userId"] == 5
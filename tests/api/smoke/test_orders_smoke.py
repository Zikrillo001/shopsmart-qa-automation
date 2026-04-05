import pytest

from src.schemas.order_schema import ORDER_SCHEMA
from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.smoke
def test_get_order_by_id_returns_valid_order(orders_client):
    response = orders_client.get_order_by_id(1)

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()
    ResponseValidator.validate_schema(response_data, ORDER_SCHEMA)

    assert response_data["id"] == 1


@pytest.mark.api
@pytest.mark.smoke
def test_create_order_returns_success(orders_client):
    payload_products = [
        {
            "productId": 2,
            "quantity": 1
        }
    ]

    response = orders_client.create_order(
        user_id=7,
        date="2026-04-05",
        products=payload_products,
    )

    assert response.status_code in [200, 201]

    response_data = response.json()
    assert response_data["userId"] == 7
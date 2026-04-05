import pytest

from src.schemas.product_schema import PRODUCT_LIST_SCHEMA, PRODUCT_SCHEMA
from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.smoke
def test_get_all_products_returns_200_and_valid_schema(products_client):
    response = products_client.get_all_products()

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()
    ResponseValidator.validate_schema(response_data, PRODUCT_LIST_SCHEMA)

    assert len(response_data) > 0


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_product_returns_valid_product(products_client):
    response = products_client.get_single_product(1)

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()

    ResponseValidator.validate_schema(response_data, PRODUCT_SCHEMA)

    assert response_data["id"] == 1
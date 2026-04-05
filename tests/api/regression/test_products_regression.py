import pytest

from src.schemas.product_schema import PRODUCT_SCHEMA
from src.utils.response_validator import ResponseValidator


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("product_id", [1, 2, 3, 10])
def test_get_multiple_products_returns_valid_schema(products_client, product_id):
    response = products_client.get_single_product(product_id)

    ResponseValidator.validate_status_code(response.status_code, 200)

    response_data = response.json()
    ResponseValidator.validate_schema(response_data, PRODUCT_SCHEMA)

    assert response_data["id"] == product_id
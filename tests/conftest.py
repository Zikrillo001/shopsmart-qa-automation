import pytest

from src.clients.auth_client import AuthClient
from src.clients.cart_client import CartClient
from src.clients.orders_client import OrdersClient
from src.clients.products_client import ProductsClient
from src.utils.config_reader import ConfigReader




@pytest.fixture(scope="session")
def config():
    reader = ConfigReader("config/config.yaml")
    return reader.config_data


@pytest.fixture(scope="session")
def api_base_url(config):
    return config["api_base_url"]


@pytest.fixture(scope="session")
def auth_client(api_base_url):
    return AuthClient(api_base_url)


@pytest.fixture(scope="session")
def products_client(api_base_url):
    return ProductsClient(api_base_url)


@pytest.fixture(scope="session")
def cart_client(api_base_url):
    return CartClient(api_base_url)


@pytest.fixture(scope="session")
def orders_client(api_base_url):
    return OrdersClient(api_base_url)
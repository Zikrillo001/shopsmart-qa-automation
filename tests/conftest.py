import pytest
from playwright.sync_api import Playwright, sync_playwright

from src.clients.auth_client import AuthClient
from src.clients.cart_client import CartClient
from src.clients.orders_client import OrdersClient
from src.clients.products_client import ProductsClient
from src.utils.config_reader import ConfigReader
import os
from datetime import datetime


@pytest.fixture(scope="session")
def config():
    reader = ConfigReader("config/config.yaml")
    return reader.config_data


@pytest.fixture(scope="session")
def api_base_url(config):
    return config["api_base_url"]


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def timeout(config):
    return config.get("timeout", 10)


@pytest.fixture(scope="session")
def auth_client(api_base_url, timeout):
    return AuthClient(api_base_url, timeout=timeout)


@pytest.fixture(scope="session")
def products_client(api_base_url, timeout):
    return ProductsClient(api_base_url, timeout=timeout)


@pytest.fixture(scope="session")
def cart_client(api_base_url, timeout):
    return CartClient(api_base_url, timeout=timeout)


@pytest.fixture(scope="session")
def orders_client(api_base_url, timeout):
    return OrdersClient(api_base_url, timeout=timeout)


@pytest.fixture(scope="session")
def auth_token(auth_client):
    response = auth_client.login(
        username="emilys",
        password="emilyspass",
    )
    response_data = response.json()
    return response_data["accessToken"]


@pytest.fixture(scope="session")
def authorized_products_client(api_base_url, timeout, auth_token):
    return ProductsClient(api_base_url, token=auth_token, timeout=timeout)


@pytest.fixture(scope="session")
def authorized_cart_client(api_base_url, timeout, auth_token):
    return CartClient(api_base_url, token=auth_token, timeout=timeout)


@pytest.fixture(scope="session")
def authorized_orders_client(api_base_url, timeout, auth_token):
    return OrdersClient(api_base_url, token=auth_token, timeout=timeout)


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance, config):
    browser_name = config.get("browser", "chromium")

    ci_mode = os.getenv("CI", "false").lower() == "true"
    headless = True if ci_mode else config.get("headless", True)

    if browser_name == "firefox":
        browser = playwright_instance.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright_instance.webkit.launch(headless=headless)
    else:
        browser = playwright_instance.chromium.launch(headless=headless)

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser, base_url):
    context = browser.new_context(record_video_dir="reports/videos/")
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: critical happy path tests")
    config.addinivalue_line("markers", "regression: broader regression coverage")
    config.addinivalue_line("markers", "api: api automation tests")
    config.addinivalue_line("markers", "ui: ui automation tests")
    config.addinivalue_line("markers", "unit: unit tests")
    config.addinivalue_line("markers", "integration: integration tests")


def pytest_runtest_logstart(nodeid, location):
    print(f"\n[START] {nodeid}")


def pytest_runtest_logfinish(nodeid, location):
    print(f"[FINISH] {nodeid}")


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        outcome = call.excinfo

        if outcome is not None:
            page = item.funcargs.get("page", None)

            if page:
                screenshots_dir = "reports/screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{item.name}_{timestamp}.png"
                file_path = os.path.join(screenshots_dir, file_name)

                page.screenshot(path=file_path)
                print(f"\n[SCREENSHOT SAVED] {file_path}")
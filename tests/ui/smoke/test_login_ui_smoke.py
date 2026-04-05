import pytest

from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_standard_user_can_login_successfully(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login(
        username="standard_user",
        password="secret_sauce",
    )

    assert inventory_page.is_inventory_loaded() is True
    assert "inventory" in inventory_page.get_url()


@pytest.mark.ui
@pytest.mark.smoke
def test_invalid_user_cannot_login(page):
    login_page = LoginPage(page)

    login_page.login(
        username="locked_out_user123",
        password="wrong_password",
    )

    assert login_page.is_error_visible() is True
import pytest

from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.regression
def test_user_can_logout_successfully(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_inventory_loaded()

    inventory_page.logout()

    assert "saucedemo.com" in page.url
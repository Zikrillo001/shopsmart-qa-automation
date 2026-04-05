import pytest

from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.regression
def test_inventory_has_products(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("standard_user", "secret_sauce")

    count = inventory_page.get_inventory_count()

    assert count > 0
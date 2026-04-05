import pytest

from src.ui.pages.login_page import LoginPage
from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.regression
def test_user_can_complete_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.click_checkout()

    cart_page.fill_checkout_info("John", "Doe", "12345")
    cart_page.finish_checkout()

    assert cart_page.is_order_complete()
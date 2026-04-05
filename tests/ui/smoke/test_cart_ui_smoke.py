import pytest

from src.ui.pages.cart_page import CartPage
from src.ui.pages.inventory_page import InventoryPage
from src.ui.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_user_can_add_product_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login(
        username="standard_user",
        password="secret_sauce",
    )

    assert inventory_page.is_inventory_loaded() is True

    inventory_page.add_backpack_to_cart()
    assert inventory_page.is_backpack_added() is True
    assert inventory_page.get_cart_badge_text() == "1"

    inventory_page.open_cart()

    assert cart_page.is_cart_loaded() is True
    assert cart_page.get_cart_items_count() == 1
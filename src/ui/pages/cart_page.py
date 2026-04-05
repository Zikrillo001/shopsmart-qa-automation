from src.ui.pages.base_page import BasePage


class CartPage(BasePage):
    CART_LIST = ".cart_list"
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"

    def is_cart_loaded(self) -> bool:
        return self.is_visible(self.CART_LIST)

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)
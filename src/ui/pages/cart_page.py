from src.ui.pages.base_page import BasePage


class CartPage(BasePage):
    CART_LIST = ".cart_list"
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def is_cart_loaded(self) -> bool:
        return self.is_visible(self.CART_LIST)

    def get_cart_items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)
    
    def fill_checkout_info(self, first, last, postal):
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)


    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)


    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)
from src.ui.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = "[data-test='inventory-container']"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    REMOVE_BACKPACK = "#remove-sauce-labs-backpack"
    CART_BADGE = ".shopping_cart_badge"
    INVENTORY_ITEMS = ".inventory_item"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def is_inventory_loaded(self) -> bool:
        return self.is_visible(self.INVENTORY_CONTAINER)

    def add_backpack_to_cart(self) -> None:
        self.click(self.ADD_TO_CART_BACKPACK)

    def is_backpack_added(self) -> bool:
        return self.is_visible(self.REMOVE_BACKPACK)

    def open_cart(self) -> None:
        self.click(self.SHOPPING_CART_LINK)

    def get_cart_badge_text(self) -> str:
        return self.get_text(self.CART_BADGE)

    def get_inventory_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEMS).count()
    
    def logout(self):
        self.click(self.MENU_BUTTON)
        self.page.wait_for_timeout(500)
        self.click(self.LOGOUT_LINK)
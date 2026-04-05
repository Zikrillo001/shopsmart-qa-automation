from playwright.sync_api import Page


class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page

    def open_cart(self) -> None:
        self.page.locator(".shopping_cart_link").click()

    def get_cart_badge_text(self) -> str:
        return self.page.locator(".shopping_cart_badge").inner_text()
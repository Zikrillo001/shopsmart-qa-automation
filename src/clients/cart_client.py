from requests import Response

from src.clients.base_client import BaseClient


class CartClient(BaseClient):
    def get_all_carts(self) -> Response:
        return self.get("/carts")

    def get_single_cart(self, cart_id: int) -> Response:
        return self.get(f"/carts/{cart_id}")

    def create_cart(self, user_id: int, date: str, products: list[dict]) -> Response:
        payload = {
            "userId": user_id,
            "date": date,
            "products": products,
        }
        return self.post("/carts/add", json=payload)
from requests import Response

from src.clients.base_client import BaseClient


class OrdersClient(BaseClient):
    def create_order(self, user_id: int, date: str, products: list[dict]) -> Response:
        payload = {
            "userId": user_id,
            "date": date,
            "products": products,
        }
        return self.post("/carts/add", json=payload)

    def get_order_history(self) -> Response:
        return self.get("/carts")

    def get_order_by_id(self, order_id: int) -> Response:
        return self.get(f"/carts/{order_id}")
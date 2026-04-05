from requests import Response

from src.clients.base_client import BaseClient


class ProductsClient(BaseClient):
    def get_all_products(self) -> Response:
        return self.get("/products")

    def get_single_product(self, product_id: int) -> Response:
        return self.get(f"/products/{product_id}")

    def get_categories(self) -> Response:
        return self.get("/products/categories")

    def get_products_by_category(self, category_name: str) -> Response:
        return self.get(f"/products/category/{category_name}")
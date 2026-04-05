CART_PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "quantity": {"type": "number"}
    },
    "required": ["id", "title", "price", "quantity"]
}

CART_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "products": {
            "type": "array",
            "items": CART_PRODUCT_SCHEMA
        }
    },
    "required": ["id", "userId", "products"]
}
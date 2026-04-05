ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "userId": {"type": "number"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "title": {"type": "string"},
                    "price": {"type": "number"},
                    "quantity": {"type": "number"}
                },
                "required": ["id", "title", "price", "quantity"]
            }
        }
    },
    "required": ["id", "userId", "products"]
}
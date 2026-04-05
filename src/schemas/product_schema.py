PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "thumbnail": {"type": "string"}   # ❗ image emas
    },
    "required": ["id", "title", "price", "description", "category", "thumbnail"]
}

PRODUCT_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "products": {
            "type": "array",
            "items": PRODUCT_SCHEMA
        },
        "total": {"type": "number"},
        "skip": {"type": "number"},
        "limit": {"type": "number"}
    },
    "required": ["products", "total", "skip", "limit"]
}
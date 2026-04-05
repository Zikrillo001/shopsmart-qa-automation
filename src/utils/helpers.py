from datetime import datetime
from typing import Any
import random
import string


def is_not_empty(value: Any) -> bool:
    return value is not None and value != ""


def generate_random_email(prefix: str = "testuser") -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{prefix}_{timestamp}_{suffix}@example.com"


def generate_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def build_headers(token: str | None = None) -> dict[str, str]:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def assert_status_code(actual: int, expected: int) -> None:
    if actual != expected:
        raise AssertionError(f"Expected status code {expected}, but got {actual}")
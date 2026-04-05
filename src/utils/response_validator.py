from typing import Any

from jsonschema import validate, ValidationError

from src.utils.exceptions import ResponseValidationError


class ResponseValidator:
    @staticmethod
    def validate_schema(data: Any, schema: dict) -> None:
        try:
            validate(instance=data, schema=schema)
        except ValidationError as exc:
            raise ResponseValidationError(f"Schema validation failed: {exc.message}") from exc

    @staticmethod
    def validate_status_code(actual: int, expected: int) -> None:
        if actual != expected:
            raise ResponseValidationError(
                f"Expected status code {expected}, but got {actual}"
            )
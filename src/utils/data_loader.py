import json
from pathlib import Path
from typing import Any

from src.utils.exceptions import DataLoadError
from src.utils.logger import get_logger


logger = get_logger(__name__)


class DataLoader:
    @staticmethod
    def load_json(file_path: str) -> Any:
        path = Path(file_path)

        if not path.exists():
            raise DataLoadError(f"Test data file not found: {file_path}")

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise DataLoadError(f"Invalid JSON in file {file_path}: {exc}") from exc

        logger.info("Loaded test data file: %s", file_path)
        return data
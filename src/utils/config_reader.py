from pathlib import Path
from typing import Any

import yaml

from src.utils.exceptions import ConfigError
from src.utils.logger import get_logger


logger = get_logger(__name__)


class ConfigReader:
    def __init__(self, config_path: str = "config/config.yaml") -> None:
        self.config_path = Path(config_path)
        self.config_data = self._load_yaml(self.config_path)

    def _load_yaml(self, file_path: Path) -> dict[str, Any]:
        if not file_path.exists():
            raise ConfigError(f"Config file not found: {file_path}")

        try:
            with file_path.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or {}
        except yaml.YAMLError as exc:
            raise ConfigError(f"Invalid YAML in file {file_path}: {exc}") from exc

        if not isinstance(data, dict):
            raise ConfigError(f"Config file must contain a dictionary: {file_path}")

        logger.info("Loaded config file: %s", file_path)
        return data

    def load_environment(self, env_name: str) -> dict[str, Any]:
        env_path = Path("config/environments") / f"{env_name}.yaml"
        env_data = self._load_yaml(env_path)
        merged = {**self.config_data, **env_data}

        logger.info("Loaded environment config: %s", env_name)
        return merged

    def get(self, key: str, default: Any = None) -> Any:
        return self.config_data.get(key, default)
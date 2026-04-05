import pytest

from src.utils.config_reader import ConfigReader
from src.utils.exceptions import ConfigError


def test_config_reader_loads_main_config(tmp_path):
    config_dir = tmp_path / "config"
    config_dir.mkdir()

    config_file = config_dir / "config.yaml"
    config_file.write_text(
        "project_name: Test Project\nbase_url: https://example.com\n",
        encoding="utf-8",
    )

    reader = ConfigReader(str(config_file))

    assert reader.get("project_name") == "Test Project"
    assert reader.get("base_url") == "https://example.com"


def test_config_reader_raises_error_for_missing_file():
    with pytest.raises(ConfigError):
        ConfigReader("missing_config.yaml")
import json

import pytest

from src.utils.data_loader import DataLoader
from src.utils.exceptions import DataLoadError


def test_load_json_success(tmp_path):
    sample_file = tmp_path / "sample.json"
    sample_data = {"name": "John", "role": "user"}
    sample_file.write_text(json.dumps(sample_data), encoding="utf-8")

    result = DataLoader.load_json(str(sample_file))

    assert result == sample_data


def test_load_json_raises_error_for_missing_file():
    with pytest.raises(DataLoadError):
        DataLoader.load_json("missing_file.json")
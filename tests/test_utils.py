import json
from unittest.mock import mock_open, patch

import src.utils as utils


def test_transactions_from_json():
    # проверка на не список (пустой)
    mock_data = {"key": "value"}
    mock_json = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = utils.transactions_from_json("dummy_path.json")
    assert result == []

    # проверка на список
    mock_data = [{"key": "value"}]
    mock_json = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = utils.transactions_from_json("dummy_path.json")
    assert result == mock_data

    # проверка на ошибку в чтении json
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("json.load", side_effect=json.JSONDecodeError("Error", "doc", 0)):
            result = utils.transactions_from_json("invalid.json")
    assert result == []

    # проверка на отсутствие файла
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = utils.transactions_from_json("nonexistent.json")
    assert result == []

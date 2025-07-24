import csv
from unittest.mock import mock_open, patch

import src.file_reader as fr


def test_csv_reader(transaction_list, transaction_csv):
    # корректное чтение
    with patch("builtins.open", mock_open(read_data=transaction_csv)):
        result = fr.csv_reader("dummy_path.csv")
    assert result == transaction_list

    # ошибки парсинга csv-файла
    with patch("builtins.open", mock_open(read_data="invalid csv")):
        with patch("csv.DictReader", side_effect=csv.Error("Error", "doc", 0)):
            result = fr.csv_reader("invalid.csv")
    assert result == []

    # проверка на отсутствие файла
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = fr.csv_reader("nonexistent.csv")
    assert result == []

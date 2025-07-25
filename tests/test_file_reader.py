from unittest.mock import patch

import pandas

import src.file_reader as fr


def test_csv_reader():
    # корректное чтение
    test_data = pandas.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    with patch("pandas.read_csv", return_value=test_data):
        result = fr.csv_reader("valid.csv")
        assert result == [{"a": 1, "b": 2}, {"a": 3, "b": 4}]

    # ошибки парсинга excel-файла
    with patch("pandas.read_csv", side_effect=pandas.errors.EmptyDataError()):
        result = fr.csv_reader("invalid.csv")
    assert result == []

    # проверка на отсутствие файла
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = fr.csv_reader("nonexistent.csv")
    assert result == []


def test_excel_reader():
    # корректное чтение
    test_data = pandas.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    with patch("pandas.read_excel", return_value=test_data):
        result = fr.excel_reader("valid.xlsx")
        assert result == [{"a": 1, "b": 2}, {"a": 3, "b": 4}]

    # ошибки парсинга excel-файла
    with patch("pandas.read_excel", side_effect=pandas.errors.EmptyDataError()):
        result = fr.excel_reader("invalid.xlsx")
    assert result == []

    # проверка на отсутствие файла
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = fr.excel_reader("nonexistent.xlsx")
    assert result == []

import pandas as pd


def csv_reader(filename: str = "") -> list[dict]:
    """
    Функция получения списка транзакций из файла csv
    :param filename: путь к файлу
    :return: список транзакций
    """
    try:
        reader = pd.read_csv(filename, delimiter=";")
        transactions = reader.to_dict(orient="records")
        return transactions
    except Exception:
        return []


def excel_reader(filename: str = "") -> list[dict]:
    """
    Функция получения списка транзакций из файла excel
    :param filename: путь к файлу
    :return: список транзакций
    """
    try:
        reader = pd.read_excel(filename)
        transactions = reader.to_dict(orient="records")
        return transactions
    except Exception:
        return []

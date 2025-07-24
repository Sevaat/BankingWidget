import csv


def csv_reader(filename: str = "") -> list[dict]:
    """
    Функция получения списка транзакций из файла csv
    :param filename: путь к файлу
    :return: список транзакций
    """
    try:
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=";")
            transactions = [row for row in reader]
            return transactions
    except Exception:
        return []

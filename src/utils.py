import json


def transactions_from_json(filename: str = "") -> list[dict]:
    """
    Функция чтения файла json для получения данных транзакций
    :param filename: путь к файлу json
    :return: данные транзакций
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            else:
                return data
    except Exception:
        return []

import re


def search_by_string(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Функция поиска транзакций с заданным описанием
    :param transactions: список транзакций
    :param search_string: описание для поиска
    :return: транзакции с заданным описанием
    """
    try:
        result = []
        for transaction in transactions:
            search_result = re.search(search_string, transaction["description"], flags=re.I)
            if search_result is not None:
                result.append(transaction)
        return result
    except Exception:
        return []

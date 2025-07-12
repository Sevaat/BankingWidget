from typing import Any, Generator


def filter_by_currency(transactions: list[dict] = [], currency: str = "") -> Generator[dict, Any, None]:
    """
    Функция, который поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions: данные транзакций
    :param currency: заданная валюта
    :return: генератор с транзакциями, где валюта операций соответствует заданной
    """
    return (tr for tr in transactions if tr["operationAmount"]["currency"]["code"] == currency)

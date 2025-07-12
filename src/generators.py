from typing import Any, Generator


def filter_by_currency(transactions: list[dict] = [], currency: str = "") -> Generator[dict, Any, None]:
    """
    Функция, который поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions: данные транзакций
    :param currency: заданная валюта
    :return: генератор с транзакциями, где валюта операций соответствует заданной
    """
    return (tr for tr in transactions if tr["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict] = []) -> Generator[dict, Any, None]:
    """
    Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    :param transactions: данные транзакций
    :return: описания каждой операции по очереди
    """
    return (tr["description"] for tr in transactions)

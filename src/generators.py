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
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """
    Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    :param start: начальный номер генерации
    :param stop: конечный номер генерации
    :return: номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    numbers = []
    for n in range(start, stop + 1):
        numbers.append(str(n).rjust(16, "0"))
    return (f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}" for number in numbers)

from collections import Counter


def category_counter(transactions: list[dict], descriptions: list) -> dict:
    """
    Функция для подсчета операций по описаниям
    :param transactions: список операций
    :param descriptions: описания для подсчета
    :return: заданные описания и их количества
    """
    try:
        zero_dictionary = {description: 0 for description in descriptions}
        result_counter = dict(Counter([t["description"] for t in transactions if t["description"] in descriptions]))
        result = {**zero_dictionary, **result_counter}
        return result
    except Exception:
        return {}

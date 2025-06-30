from datetime import datetime


def filter_by_state(datas: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрации списка словарей по ключу "state"
    :param datas: список словарей
    :param state: значение ключа
    :return: список словарей с ключом "state"
    """
    datas_with_key = [data for data in datas if "state" in data]
    return [data for data in datas_with_key if data["state"] == state]


def sort_by_date(datas: list[dict], order: bool = True) -> list[dict]:
    """
    Функция сортировки списка словарей по ключу "date"
    :param datas: список словарей
    :param order: порядок сортировки (True - по убыванию, False - по возрастанию)
    :return: упорядоченный список словарей по ключу "date"
    """
    datas_with_date = [data for data in datas if "date" in data]
    ordered_datas = sorted(datas_with_date, key=lambda data: datetime.fromisoformat(data["date"]), reverse=order)
    for data in datas:
        if data not in datas_with_date:
            ordered_datas.append(data)
    return ordered_datas


if __name__ == "__main__":
    pass

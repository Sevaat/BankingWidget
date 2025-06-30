def filter_by_state(datas: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрации списка словарей по ключу "state"
    :param datas: список словарей
    :param state: значение ключа
    :return: список словарей с ключом "state"
    """
    datas_with_key = [data for data in datas if "state" in data]
    return [data for data in datas_with_key if data["state"] == state]


if __name__ == "__main__":
    pass

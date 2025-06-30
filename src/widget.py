from datetime import datetime

import src.masks as masks


def mask_account_card(user_payment_details: str) -> str:
    """
    Функция маскировки платежных данных пользователя
    :param user_payment_details: платежные данные пользователя (карта номер, счет номер)
    :return: замаскированные платежных данных пользователя
    """
    upd = user_payment_details.split()
    if len(upd[-1]) == 16:
        upd[-1] = masks.get_mask_card_number(int(upd[-1]))
    else:
        upd[-1] = masks.get_mask_account(int(upd[-1]))
    return " ".join(upd)


def get_date(user_date: str) -> str:
    """
    Функция преобразования даты из стандартного представления времени
    :param user_date: дата из стандартного представления времени
    :return: дата в формате "ДД.ММ.ГГГГ"
    """
    date = datetime.fromisoformat(user_date)
    return date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    pass

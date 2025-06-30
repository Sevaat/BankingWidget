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


if __name__ == "__main__":
    pass

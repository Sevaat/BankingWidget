def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты
    :return: замаскированный номер карты
    """
    str_card_number = str(card_number)
    masked_сard_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return masked_сard_number


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: номер счета
    :return: замаскированный номер счета
    """
    str_account_number = str(account_number)
    disguised_account_number = f"**{str_account_number[-4:]}"
    return disguised_account_number


if __name__ == "__main__":
    pass

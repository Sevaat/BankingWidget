def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты
    :return: замаскированный номер карты
    """
    str_card_number = str(card_number)
    masked_сard_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return masked_сard_number


if __name__ == "__main__":
    pass

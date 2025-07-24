import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
log_dir = os.path.abspath("../logs")
os.makedirs(log_dir, exist_ok=True)
file_handler = logging.FileHandler(filename=f"{log_dir}/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера банковской карты
    :param card_number: номер карты
    :return: замаскированный номер карты
    """
    try:
        str_card_number = str(card_number)
        if len(str_card_number) == 16:
            logger.info("Номер карты имеет корректный формат")
            masked_сard_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
            return masked_сard_number
        else:
            logger.info(f"Номер карты имеет некорректный формат: {len(str_card_number)} != 16")
            return "**** **** **** ****"
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "**** **** **** ****"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскировки номера банковского счета
    :param account_number: номер счета
    :return: замаскированный номер счета
    """
    try:
        str_account_number = str(account_number)
        if len(str_account_number) == 20:
            logger.info("Номер счета имеет корректный формат")
            disguised_account_number = f"**{str_account_number[-4:]}"
            return disguised_account_number
        else:
            logger.info(f"Номер счета имеет некорректный формат: {len(str_account_number)} != 20")
            return "******"
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "******"

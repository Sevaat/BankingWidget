import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_from_json(filename: str = "") -> list[dict]:
    """
    Функция чтения файла json для получения данных транзакций
    :param filename: путь к файлу json
    :return: данные транзакций
    """
    try:
        data = None
        with open(filename, "r") as file:
            data = json.load(file)
        logger.info("Данные файла json считаны успешно")
        if not isinstance(data, list):
            logger.info("Загруженные данные не являются списком")
            return []
        else:
            logger.info("Данные файла json загружены успешно")
            return data
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []

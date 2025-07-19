import json
import os

import requests
from dotenv import load_dotenv


def currency_conversions(transaction: dict) -> float:
    """
    Функция конвертации суммы транзакции в рубли
    :param transaction: транзакция
    :return: сумма транзакции в рублях
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    response = requests.request("GET", url, headers=headers, data={})
    result = json.loads(response.text)

    return float(result["result"])

if __name__ == '__main__':
    mock_data = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}},}
    print(currency_conversions(mock_data))

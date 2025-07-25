import src.file_reader as fr
import src.generators as generators
import src.processing as processing
import src.search_engine as se
import src.utils as utils
import src.widget as widget

receiving_transactions = {
    "1": ["Получить информацию о транзакциях из JSON-файла", utils.transactions_from_json],
    "2": ["Получить информацию о транзакциях из CSV-файла", fr.csv_reader],
    "3": ["Получить информацию о транзакциях из XLSX-файла", fr.excel_reader],
}


def main() -> None:
    """
    Функция, предоставляющая пользовательский интерфейс для работы с программой
    :return:
    """
    # диалог №1
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню (введите номер пункта):
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    answer = None
    while True:
        answer = input()
        if answer in ["1", "2", "3"]:
            break
        else:
            print(f'Введенный вами пункт "{answer}" некорректный. Повторите попытку')
    print(f"{receiving_transactions[answer][0]}")
    print()

    # диалог №2
    print("Укажите путь к файлу")
    filename = None
    transactions = None
    while True:
        filename = input()
        transactions = receiving_transactions[answer][1](filename)
        if transactions:
            print(f'С заданного пути "{filename}" данные успешно загружены')
            break
        else:
            print(f'Введенный вами путь "{filename}" некорректный. Повторите попытку')
    print()

    # диалог №3
    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    answer = None
    while True:
        answer = input().upper()
        if answer in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = processing.filter_by_state(transactions, answer)
            print(f'Операции отфильтрованы по статусу "{answer}"')
            break
        else:
            print(f'Введенный вами статус "{answer}" некорректный. Повторите попытку')
    print()

    # диалог №4
    print("Отсортировать операции по дате? Да/Нет")
    answer = None
    while True:
        answer = input().upper()
        if answer in ["ДА", "НЕТ"]:
            break
        else:
            print(f'Введенный вами ответ "{answer}" некорректный. Повторите попытку')
    if answer == "ДА":
        print("Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию")
        answer = None
        while True:
            answer = input().upper()
            if answer in ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"]:
                transactions = processing.sort_by_date(transactions, answer == "ПО УБЫВАНИЮ")
                print(f"Операции отсортированы по дате ({answer})")
                break
            else:
                print(f'Введенный вами ответ "{answer}" некорректный. Повторите попытку')
    print()

    # диалог №5
    print("Выводить только рублевые транзакции? Да/Нет")
    answer = None
    while True:
        answer = input().upper()
        if answer in ["ДА", "НЕТ"]:
            transactions = list(generators.filter_by_currency(transactions, "RUB"))
            print('Операции отфильтрованы по валюте "RUB"')
            break
        else:
            print(f'Введенный вами ответ "{answer}" некорректный. Повторите попытку')
    print()

    # диалог №6
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer = None
    while True:
        answer = input().upper()
        if answer in ["ДА", "НЕТ"]:
            break
        else:
            print(f'Введенный вами ответ "{answer}" некорректный. Повторите попытку')
    if answer == "ДА":
        print("По какому слову в описании транзакции отфильтровать?")
        answer = input()
        transactions = se.search_by_string(transactions, answer)
        print(f'Операции отфильтрованы по слову "{answer}" в описании')
    print()

    # диалог №7
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        print("Распечатываю итоговый список транзакций...")
        text = []
        for transaction in transactions:
            text.append(f"{widget.get_date(transaction['date'])} {transaction['description']}")
            if transaction["description"] == "Открытие вклада":
                account = transaction["to"].split()
                text.append(f"{account[0]} {widget.mask_account_card(account[1])}")
            else:
                account_card_1 = transaction["from"].split()
                account_card_1 = f"{account_card_1[:-1]} {widget.mask_account_card(account_card_1[-1])}"
                account_card_2 = transaction["to"].split()
                account_card_2 = f"{account_card_2[:-1]} {widget.mask_account_card(account_card_2[-1])}"
                text.append(f"{account_card_1} -> {account_card_2}")
            amount = transaction["operationAmount"]["amount"]
            name = transaction["operationAmount"]["currency"]["name"]
            text.append(f"Сумма {amount} {name}")
            print()
            print("\n".join(text))
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()

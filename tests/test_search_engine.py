import src.search_engine as se


def test_search_by_string(transactions, transactions_org):
    assert se.search_by_string(transactions, "Перевод организации") == transactions_org

    assert se.search_by_string(transactions, "ПЕРЕВОД организации") == transactions_org

    assert se.search_by_string(transactions, "Не пустое поле") == []

    assert se.search_by_string(transactions, "") == transactions

import src.counter as counter


def test_category_counter(transactions):
    assert counter.category_counter(transactions, ["Перевод организации"]) == {"Перевод организации": 2}

    assert counter.category_counter(transactions, ["Перевод"]) == {"Перевод": 0}

    assert counter.category_counter(transactions, [""]) == {"": 0}

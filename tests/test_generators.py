import src.generators as gn


def test_filter_by_currency(transactions, transactions_usd, transactions_rub):
    assert list(gn.filter_by_currency(transactions, currency="USD")) == transactions_usd
    assert list(gn.filter_by_currency(transactions, currency="RUB")) == transactions_rub
    assert list(gn.filter_by_currency(transactions, currency="000")) == []
    assert list(gn.filter_by_currency(transactions)) == []
    assert list(gn.filter_by_currency(currency="000")) == []


def test_transaction_descriptions(transactions, transaction_descriptions):
    assert list(gn.transaction_descriptions(transactions)) == transaction_descriptions


def test_card_number_generator(card_number):
    assert list(gn.card_number_generator(1, 5)) == card_number

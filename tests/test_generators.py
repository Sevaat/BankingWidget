import src.generators as gn


def test_filter_by_state_executed(transactions, transactions_usd, transactions_rub):
    assert list(gn.filter_by_currency(transactions, currency="USD")) == transactions_usd
    assert list(gn.filter_by_currency(transactions, currency="RUB")) == transactions_rub
    assert list(gn.filter_by_currency(transactions, currency="000")) == []
    assert list(gn.filter_by_currency(transactions)) == []
    assert list(gn.filter_by_currency(currency="000")) == []

import pytest

import src.generators as gn


@pytest.mark.parametrize(
    "currency, result",
    [
        ("USD", 3),
        ("RUB", 2),
        ("", 0),
        ("000", 0),
    ],
)
def test_filter_by_currency(transactions, currency, result):
    assert len(list(gn.filter_by_currency(transactions, currency))) == result


def test_transaction_descriptions(transactions, transaction_descriptions):
    assert list(gn.transaction_descriptions(transactions)) == transaction_descriptions


def test_card_number_generator(card_number):
    assert list(gn.card_number_generator(1, 5)) == card_number

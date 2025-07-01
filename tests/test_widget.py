import pytest

import src.widget as widget


@pytest.mark.parametrize(
    "user_payment_details, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_card(user_payment_details, result):
    assert widget.mask_account_card(user_payment_details) == result


def test_get_date():
    assert widget.get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

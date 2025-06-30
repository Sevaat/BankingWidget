import unittest

import src.widget as widget


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number_1(self) -> None:
        result = widget.mask_account_card("Visa Platinum 7000792289606361")
        expected_result = "Visa Platinum 7000 79** **** 6361"
        self.assertEqual(result, expected_result)

    def test_get_mask_card_number_2(self) -> None:
        result = widget.mask_account_card("Счет 73654108430135874305")
        expected_result = "Счет **430"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

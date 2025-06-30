import unittest

import src.masks as masks


class TestMasks(unittest.TestCase):

    def test_get_mask_card_number(self) -> None:
        result = masks.get_mask_card_number(7000792289606361)
        expected_result = "7000 79** **** 6361"
        self.assertEqual(result, expected_result)

    def test_get_mask_account(self) -> None:
        result = masks.get_mask_account(73654108430135874305)
        expected_result = "**4305"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

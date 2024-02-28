""" Test OrderedDict Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.ordered_dict import get_summary, main


class TestOrderedDict:
    """Test OrderedDict module"""

    def test_get_summary(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_summary function is working as expected"""
        input_values = [
            "BANANA FRIES 12",
            "POTATO CHIPS 30",
            "APPLE JUICE 10",
            "CANDY 5",
            "APPLE JUICE 10",
            "CANDY 5",
            "CANDY 5",
            "CANDY 5",
            "POTATO CHIPS 30",
        ]

        transactions = 9
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        bill = get_summary(transactions)

        assert bill == {
            "BANANA FRIES": 12,
            "POTATO CHIPS": 60,
            "APPLE JUICE": 20,
            "CANDY": 20,
        }

    def test_ordered_dict_main_program(self, monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
        """Test main program is working as expected"""
        input_values = [
            "9",
            "BANANA FRIES 12",
            "POTATO CHIPS 30",
            "APPLE JUICE 10",
            "CANDY 5",
            "APPLE JUICE 10",
            "CANDY 5",
            "CANDY 5",
            "CANDY 5",
            "POTATO CHIPS 30",
        ]
        expected_output = "BANANA FRIES 12\nPOTATO CHIPS 60\nAPPLE JUICE 20\nCANDY 20\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()

        captured = capsys.readouterr()
        assert captured.out == expected_output

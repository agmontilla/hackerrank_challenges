""" Test Validating Credit Card Numbers Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.validating_credit_card_numbers import (
    CreditCardNumberCollection,
    main,
)


class TestValidatingCreditCardNumbers:
    """Test Validating Credit Card Numbers module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main"""
        input_values = [
            "6",
            "4123456789123456",
            "5123-4567-8912-3456",
            "61234-567-8912-3456",
            "4123356789123456",
            "5133-3367-8912-3456",
            "5123 - 3567 - 8912 - 3456",
        ]
        expected_output = "Valid\nValid\nInvalid\nValid\nInvalid\nInvalid\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_are_valid(self) -> None:
        """Test are_valid"""
        credit_cards = [
            "4123456789123456",
            "5123-4567-8912-3456",
            "61234-567-8912-3456",
            "4123356789123456",
            "5133-3367-8912-3456",
            "5123 - 3567 - 8912 - 3456",
        ]
        expected_output = ["Valid", "Valid", "Invalid", "Valid", "Invalid", "Invalid"]
        assert list(CreditCardNumberCollection(credit_cards).are_valid()) == expected_output

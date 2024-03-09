""" Test cases for the Validating Postal Code challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.validating_postal_codes import (
    Checkeable,
    HasAlternatingRepetitiveDigitPair,
    IsInRange,
    PostalCode,
    main,
)


class TestPostalCodeValidations:
    """Test Postal Code Validations"""

    def test_invalid_postal_code_out_of_range(self) -> None:
        """Returns False if the postal code is out of range."""
        validation = IsInRange()
        result = validation.check("12345")
        assert result is False

    def test_valid_postal_code_in_range(self) -> None:
        """Returns True if the postal code is in range."""
        validation = IsInRange()
        result = validation.check("123456")
        assert result is True

    def test_valid_postal_code_no_alternating_repetitive_digit_pair(self) -> None:
        """Returns True if the postal code has no alternating repetitive digit pair."""
        validation = HasAlternatingRepetitiveDigitPair()
        result = validation.check("121426")
        assert result is True

    def test_valid_postal_code_multiple_alternating_repetitive_digit_pairs(self) -> None:
        """Returns True if the postal code has multiple alternating repetitive digit pairs (less than 2)."""
        validation = HasAlternatingRepetitiveDigitPair()
        result = validation.check("123123")
        assert result is True

    def test_invalid_postal_code_multiple_alternating_repetitive_digit_pairs(self) -> None:
        """Returns False if the postal code has multiple alternating repetitive digit pairs (2 or more)."""
        validation = HasAlternatingRepetitiveDigitPair()
        result = validation.check("121212")
        assert result is False


class TestPostalCode:
    """Test Postal Code"""

    VALIDATORS: list[Checkeable] = [IsInRange(), HasAlternatingRepetitiveDigitPair()]

    def test_is_valid_returns_true_for_valid_postal_code(self) -> None:
        """Returns True if the postal code is valid."""
        # Arrange
        postal_code = PostalCode("121426", validations=self.VALIDATORS)

        # Act
        result = postal_code.is_valid()

        # Assert
        assert result is True

    def test_is_valid_returns_false_for_invalid_postal_code(self) -> None:
        """Returns False if the postal code is invalid."""
        # Arrange
        postal_code = PostalCode("110000", validations=self.VALIDATORS)

        # Act
        result = postal_code.is_valid()

        # Assert
        assert result is False

    def test_main(self, monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
        """Prints the result of the postal code validation."""
        # Arrange
        monkeypatch.setattr("builtins.input", lambda: "110000")
        expected_output = "False\n"

        # Act
        main()

        # Assert
        captured = capsys.readouterr()
        assert captured.out == expected_output

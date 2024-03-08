""" Test validating roman numerals challenge """

from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.regex_and_parsing.validating_roman_numerals import (
    is_a_roman_number,
    main,
)


class TestValidatingRomanNumerals:
    """Test validating roman numerals module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_ = "CDXXI"
        monkeypatch.setattr("builtins.input", lambda: input_)
        main()
        captured = capsys.readouterr()
        assert captured.out == "True\n"

    @mark.parametrize(
        "roman_number, expected",
        [
            ("CDXXI", True),
            ("OPP", False),
        ],
    )
    def test_is_a_roman_number(self, roman_number: str, expected: bool) -> None:
        """Test is_a_roman_number function"""
        assert is_a_roman_number(roman_number) is expected

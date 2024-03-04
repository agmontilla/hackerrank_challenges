""" Test Incorrect Regex Challenge"""
from pytest import CaptureFixture, MonkeyPatch

from challenges.errors_and_exceptions.incorrect_regex import is_valid_regex, main


class TestIncorrectRegex:
    """Test Incorrect Regex module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2", r".*\+", r".*+"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "True\nFalse\n"

    def test_is_valid_regex(self) -> None:
        """Test is_valid_regex function"""
        assert is_valid_regex(r".*\+") is True
        assert is_valid_regex(r".*+") is False

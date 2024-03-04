""" Test Exceptions Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.errors_and_exceptions.exceptions import main, perform_division


class TestExceptions:
    """Test Exceptions module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["3", "1 0", "2 $", "3 1"]
        output_values = ["Error Code: integer division or modulo by zero", "Error Code: invalid literal for int() with base 10: '$'", "3"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "\n".join(output_values) + "\n"

    def test_perform_division(self) -> None:
        """Test perform_division function"""
        assert perform_division(1, 0) == "Error Code: integer division or modulo by zero"
        assert perform_division(2, "$") == "Error Code: invalid literal for int() with base 10: '$'"
        assert perform_division(3, 1) == 3

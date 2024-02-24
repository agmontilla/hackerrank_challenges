""" Test cases for ArithmeticOperators"""

from pytest import CaptureFixture, MonkeyPatch

from challenges.introduction.arithmetic_operators import (
    main,
    show_arithmetic_operations,
)


class TestArithmeticOperators:
    """Test cases for ArithmeticOperators module"""

    def test_show_arithmetic_operations(self, capsys: CaptureFixture) -> None:
        """Show arithmetic operations"""
        # Arrange
        expected_output = "5\n1\n6\n"

        # Act
        show_arithmetic_operations(3, 2)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected_output

    def test_show_arithmetic_operations_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Show arithmetic operations main program is working"""
        # Arrange
        input_values = ["3", "2"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected_output = "5\n1\n6\n"

        # Act
        main()

        # Assert
        out, _ = capsys.readouterr()
        assert out == expected_output

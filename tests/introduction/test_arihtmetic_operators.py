""" Test cases for ArithmeticOperators"""

from pytest import CaptureFixture

from challenges.introduction.arithmetic_operators import show_arithmetic_operations


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

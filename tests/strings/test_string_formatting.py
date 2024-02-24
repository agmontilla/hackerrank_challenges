""" Test cases for string formatting """
from pytest import CaptureFixture

from challenges.strings.string_formatting import print_formatted


class TestPrintFormatting:
    """Test cases for the print_formatted function"""

    def test_print_formatting_is_working(self, capsys: CaptureFixture) -> None:
        """print_formatted is working as expected"""
        print_formatted(2)
        captured = capsys.readouterr()
        assert captured.out == " 1  1  1  1\n 2  2  2 10\n"

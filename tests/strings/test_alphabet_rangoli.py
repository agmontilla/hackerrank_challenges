""" Test cases for the alphabet_rangoli module. """
from pytest import CaptureFixture

from python.strings.alphabet_rangoli import print_rangoli


class TestAlphabetRangoli:
    """Test cases for the print_rangoli function"""

    def test_alphabet_rangoli_is_working(self, capfd: CaptureFixture) -> None:
        """print_rangoli is working as expected"""
        expected = "----c----\n--c-b-c--\nc-b-a-b-c\n--c-b-c--\n----c----\n"
        print_rangoli(3)
        out, _ = capfd.readouterr()
        assert out == expected

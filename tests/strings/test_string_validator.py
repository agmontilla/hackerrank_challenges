""" Test cases for string validator """
from pytest import CaptureFixture

from python.strings.string_validators import check_string


class TestStringValidator():
    """ Test cases for the check_string function """

    def test_string_validator_is_working(self, capsys: CaptureFixture) -> None:
        """ check_string is working as expected """
        check_string('qA2')
        captured = capsys.readouterr()
        assert captured.out == 'True\nTrue\nTrue\nTrue\nTrue\n'

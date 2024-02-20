""" Test for the WhatsYourName module """
from pytest import CaptureFixture

from python.strings.whats_your_name import print_full_name


class TestWhatsYourName():
    """ Test cases for the print_full_name function """

    def test_whats_your_name_is_working(self, capsys: CaptureFixture) -> None:
        """ print_full_name is working as expected """
        # Arrange
        first_name = 'Ross'
        last_name = 'Taylor'

        expected = 'Hello Ross Taylor! You just delved into python.\n'

        # Act
        print_full_name(first_name, last_name)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected

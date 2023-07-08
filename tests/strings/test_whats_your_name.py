from pytest import CaptureFixture
from python.strings.whats_your_name import print_full_name


class TestWhatsYourName():

    def test_whats_your_name_is_working(self, capsys: CaptureFixture) -> None:
        # Arrange
        first_name = 'Ross'
        last_name = 'Taylor'

        expected = 'Hello Ross Taylor! You just delved into python.\n'

        # Act
        print_full_name(first_name, last_name)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected

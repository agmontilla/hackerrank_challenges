""" Test cases for the text_wrap module. """
from python.strings.text_wrap import wrap


class TestWrap():
    """ Test cases for the text_wrap module """

    def test_wrap_is_working(self) -> None:
        """ Test if wrap is working as expected """
        # Arrange
        string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
        max_width = 4
        expected = "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"

        # Act
        result = wrap(string, max_width)

        # Assert
        assert result == expected

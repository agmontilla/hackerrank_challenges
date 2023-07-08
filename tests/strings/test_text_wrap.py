from python.strings.text_wrap import wrap


class TestWrap():

    def test_wrap_is_working(self) -> None:
        # Arrange
        string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
        max_width = 4
        expected = "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"

        # Act
        result = wrap(string, max_width)

        # Assert
        assert result == expected

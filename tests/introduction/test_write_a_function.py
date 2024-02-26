""" Tests for the Write A Function challenge """

from challenges.introduction.write_a_function import is_leap


class TestWriteAFunction:
    """Tests for the Write A Function challenge"""

    def test_is_leap(self) -> None:
        """Test is_leap is working as expected"""
        assert is_leap(1990) is False
        assert is_leap(2000) is True

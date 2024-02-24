""" Test for the capitalize module """
from challenges.strings.capitalize import solve


class TestCapitalize:
    """Test cases for the solve function"""

    def test_capitalize_is_working(self) -> None:
        """capitalize is working as expected"""
        assert solve("hello world") == "Hello World"

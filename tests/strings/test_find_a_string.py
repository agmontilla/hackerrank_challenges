""" Test cases for find_a_string.py """
from python.strings.find_a_string import count_substring


class TestFindAString():
    """ Test cases for count_substring function """

    def test_count_substring(self) -> None:
        """ count_substring is working as expected """
        assert count_substring('ABCDCDC', 'CDC') == 2

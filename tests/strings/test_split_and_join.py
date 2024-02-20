""" Test cases for the split_and_join module. """
from python.strings.split_and_join import split_and_join


class TestSplitAndJoin():
    """ Test cases for the split_and_join module """

    def test_split_and_join_is_working_as_expected(self) -> None:
        """ Test if split_and_join is working as expected """
        assert split_and_join('this is a string') == 'this-is-a-string'

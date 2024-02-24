""" Test cases for the mutations module. """
from challenges.strings.mutations import mutate_string


class TestMutations:
    """Test cases for the mutations module"""

    def test_mutations_is_working_as_expected(self) -> None:
        """Test if mutate_string is working as expected"""
        assert mutate_string("abracadabra", 5, "k") == "abrackdabra"

""" Test cases for the swap_case function """
from challenges.strings.swap_case import swap_case


class TestSwapCase:
    """Test cases for the swap_case function"""

    def test_swap_case(self) -> None:
        """swap_case is working as expected"""
        sample = 'HackerRank.com presents "Pythonist 2".'
        assert swap_case(sample) == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'


from python.strings.swap_case import swap_case


class TestSwapCase():

    def test_swap_case(self) -> None:
        sample = "HackerRank.com presents \"Pythonist 2\"."
        assert swap_case(sample) == "hACKERrANK.COM PRESENTS \"pYTHONIST 2\"."

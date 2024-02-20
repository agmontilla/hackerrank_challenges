""" Test difference of two sets """

from python.sets.difference import run_difference


class TestDifference:
    """ Test cases for difference function """

    def test_difference_operation_is_working_as_expected(self) -> None:
        """ difference operation is working as expected """
        set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        set_b = {10, 1, 2, 3, 11, 21, 55, 6, 8}
        assert run_difference(set_a, set_b) == 4

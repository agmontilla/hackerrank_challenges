""" Test cases for the strict_superset function """
from pytest import MonkeyPatch

from python.sets.check_strict_superset import check_strict_superset


class TestStrictSuperSet():
    """ Test cases for check_strict_superset function """

    def test_strict_super_set(self, monkeypatch: MonkeyPatch) -> None:
        """ Strict Super Set is working as expected """
        inputs = [
            "1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78",
            "2", "1 2 3 4 5", "100 11 12"
        ]
        monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))
        assert check_strict_superset() is False

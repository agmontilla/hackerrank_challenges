""" Test cases for intersection function"""
# pylint: disable=duplicate-code

from pytest import CaptureFixture, MonkeyPatch

from python.sets.intersection import main, run_intersection


class TestIntersection:
    """ Test cases for intersection function """

    def test_intersection_operation_is_working_as_expected(self) -> None:
        """ intersection operation is working as expected """
        set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        set_b = {10, 1, 2, 3, 11, 21, 55, 6, 8}
        assert run_intersection(set_a, set_b) == 5

    def test_print_intersection_operation(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """ print intersection operation is working as expected """
        inputs = [
            "9",
            "1 2 3 4 5 6 7 8 9",
            "9",
            "10 1 2 3 11 21 55 6 8"
        ]
        monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "5\n"

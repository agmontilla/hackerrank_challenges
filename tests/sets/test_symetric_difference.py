""" Test for symetric_difference """

from pytest import CaptureFixture, MonkeyPatch

from challenges.sets.symetric_difference import main, run_symetric_difference


class TestSymetricDifference:
    """Test for symetric_difference"""

    def test_run_symetric_difference_is_working(self) -> None:
        """Test if run_symetric_difference is working as expected"""
        sets = [[2, 4, 5, 9], [2, 4, 11, 12]]
        results = run_symetric_difference(sets)
        assert results == [5, 9, 11, 12]

    def test_run_symetric_difference_is_working_with_empty_list(self) -> None:
        """Test if run_symetric_difference is working as expected with empty list"""
        sets: list[list] = [[], []]
        results = run_symetric_difference(sets)
        assert results == []

    def test_symetric_difference_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test if symetric_difference main program is working as expected"""
        input_values = ["4", "2 4 5 9", "4", "2 4 11 12"]
        expected_output = "5\n9\n11\n12\n"

        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()

        out, _ = capsys.readouterr()
        assert out == expected_output

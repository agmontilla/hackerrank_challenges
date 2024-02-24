""" Test for union """

from pytest import CaptureFixture, MonkeyPatch

from python.sets.union import main, run_union


class TestUnion:
    """Test for union"""

    def test_run_union_is_working(self) -> None:
        """Test if run_union is working as expected"""
        set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        set_b = {10, 1, 2, 3, 11, 21, 55, 6, 8}
        results = run_union(set_a, set_b)
        assert results == 13

    def test_run_union_is_working_with_empty_set(self) -> None:
        """Test if run_union is working as expected with empty set"""
        set_a: set = set()
        set_b: set = set()
        results = run_union(set_a, set_b)
        assert results == 0

    def test_union_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test if union main program is working as expected"""
        input_values = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
        expected_output = "13\n"

        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()

        out, _ = capsys.readouterr()
        assert out == expected_output

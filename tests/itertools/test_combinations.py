""" Test Combinations Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.combinations import main, run_combinations


class TestCombinations:
    """Test Combinations Challenge"""

    def test_run_combinations(self) -> None:
        """Test run_combinations function is working as expected."""

        expected = ["A", "C", "H", "K", "AC", "AH", "AK", "CH", "CK", "HK"]
        results = run_combinations(2, "HACK")

        assert results == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected."""
        expected = "A\nC\nH\nK\nAC\nAH\nAK\nCH\nCK\nHK\n"
        monkeypatch.setattr("builtins.input", lambda: "HACK 2")

        main()

        out, _ = capsys.readouterr()
        assert out == expected

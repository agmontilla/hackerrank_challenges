""" Test for Combinations with Replacement Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.combinations_with_replacement import (
    main,
    run_combinations_with_replacement,
)


class TestCombinationWithReplacement:
    """Test Combinations with Replacement Challenge"""

    def test_run_combinations_with_replacement(self) -> None:
        """Test run_combinations_with_replacement function is working as expected."""
        expected = ["AA", "AC", "AH", "AK", "CC", "CH", "CK", "HH", "HK", "KK"]
        results = run_combinations_with_replacement(2, "HACK")
        assert results == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected."""
        expected = "AA\nAC\nAH\nAK\nCC\nCH\nCK\nHH\nHK\nKK\n"
        monkeypatch.setattr("builtins.input", lambda: "HACK 2")
        main()
        out, _ = capsys.readouterr()
        assert out == expected

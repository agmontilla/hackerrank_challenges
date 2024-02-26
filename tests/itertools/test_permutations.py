""" Tests for the itertools.permutations challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.permutations import main, run_permutations


class TestPermutations:
    """Test for the itertools.permutations challenge."""

    def test_run_permutations_is_working(self) -> None:
        """Test for the run_permutations function is working as expected."""
        results = run_permutations("HACK", 2)
        expected = ["AC", "AH", "AK", "CA", "CH", "CK", "HA", "HC", "HK", "KA", "KC", "KH"]
        assert results == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function."""
        inputs = ["HACK 2"]
        expected = "AC\nAH\nAK\nCA\nCH\nCK\nHA\nHC\nHK\nKA\nKC\nKH\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        out, _ = capsys.readouterr()

        assert out == expected

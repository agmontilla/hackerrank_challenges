""" Tests for the itertools.product challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.product import main, run_product


class TestProduct:
    """Test for the itertools.product challenge."""

    def test_run_product_is_working(self) -> None:
        """Test for the run_product function is working as expected."""
        results = run_product([1, 2], [3, 4])
        expected = [(1, 3), (1, 4), (2, 3), (2, 4)]

        assert results == expected

    def test_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected."""
        input_values = [
            "1 2",
            "3 4",
        ]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected = "(1, 3) (1, 4) (2, 3) (2, 4)\n"

        main()

        out, _ = capsys.readouterr()
        assert out == expected

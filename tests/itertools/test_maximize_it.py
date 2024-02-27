""" Tests for Maximize It! challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.maximize_it import main, maximize_it


class TestMaximizeIt:
    """Tests for Maximize It! challenge."""

    def test_maximize_it(self) -> None:
        """Should return the maximum value of the expression."""
        remain_number = "1000"
        coefs = [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]
        expected = 206

        result = maximize_it(remain_number, coefs)

        assert result == expected

    def test_maximize_it_main_program(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Should print the maximum value of the expression."""
        inputs = ["3 1000", "2 5 4", "3 7 8 9", "5 5 7 8 9 10"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()

        captured = capsys.readouterr()
        output = "206\n"
        assert captured.out == output

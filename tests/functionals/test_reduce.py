""" Test reduce challenge. """
from fractions import Fraction

from pytest import CaptureFixture, MonkeyPatch

from challenges.functionals.reduce import main, product


class TestReduce:
    """Test reduce module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function."""
        inputs = [3, "1 2", "3 4", "10 6"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "5 8\n"

    def test_product(self) -> None:
        """Test product function."""
        fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]
        assert product(fracs) == (5, 8)

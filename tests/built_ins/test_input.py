""" Test Built-in input() Challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.built_ins.input import is_divisible_by, main


class TestInput:
    """Test Built-in input() module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["1 4", "x**3 + x**2 + x + 1"]
        output = "True\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == output

    @mark.parametrize(
        "k, x, polinomial, expected",
        [
            (4, 1, "x**3 + x**2 + x + 1", True),
            (4, 1, "x**3 + x**2 + x + 2", False),
        ],
    )
    def test_is_divisible_by(self, k: int, x: int, polinomial: str, expected: bool) -> None:
        """Test is_divisible_by function"""
        assert is_divisible_by(k, x, polinomial) == expected

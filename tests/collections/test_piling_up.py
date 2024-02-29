""" Test Piling Up Challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.collections.piling_up import Cube, main


class TestPilingUp:
    """Test Piling Up module"""

    @mark.parametrize("length, elements, expected", [(6, [4, 3, 2, 1, 3, 4], "Yes"), (3, [1, 3, 2], "No")])
    def test_cube_is_pileable(self, length: int, elements: list[int], expected: str) -> None:
        """Test Cube class"""
        cube = Cube(length)
        cube.elements = elements
        assert cube.is_pileable() == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["2", "6", "4 3 2 1 3 4", "3", "1 3 2"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "Yes\nNo\n"

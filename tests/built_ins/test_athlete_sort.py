""" Test for Athlete Sort challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.built_ins.athlete_sort import main, order_by_athlete


class TestAthleteSort:
    """Test Athlete Sort module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["5 3", "10 2 5", "7 1 0", "9 9 9", "1 23 12", "6 5 9", "1"]
        outputs = "7 1 0\n10 2 5\n6 5 9\n9 9 9\n1 23 12\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == outputs

    @mark.parametrize(
        "attribute, expected",
        [
            (0, [(1, 23, 12), (6, 5, 9), (7, 1, 0), (9, 9, 9), (10, 2, 5)]),
            (1, [(7, 1, 0), (10, 2, 5), (6, 5, 9), (9, 9, 9), (1, 23, 12)]),
            (2, [(7, 1, 0), (10, 2, 5), (9, 9, 9), (6, 5, 9), (1, 23, 12)]),
        ],
    )
    def test_order_by_athlete(self, attribute: int, expected: list[tuple[int]]) -> None:
        """Test order_by_athlete function"""
        sheet = [(10, 2, 5), (7, 1, 0), (9, 9, 9), (1, 23, 12), (6, 5, 9)]
        assert order_by_athlete(sheet, attribute) == expected

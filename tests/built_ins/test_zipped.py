"""Test Zipped! Challenge"""
from pytest import CaptureFixture, MonkeyPatch

from challenges.built_ins.zipped import get_average_score, main


class TestZipped:
    """Test Zipped! module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["5 3", "89 90 78 93 80", "90 91 85 88 86", "91 92 83 89 90.5"]
        output = "90.0\n91.0\n82.0\n90.0\n85.5\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == output

    def test_get_average_score(self) -> None:
        """Test get_average_score function"""
        input_values: list[list[float]] = [[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]]
        output = [90.0, 91.0, 82.0, 90.0, 85.5]
        assert get_average_score(input_values) == output

""" Tests for the check_subset function """

from pytest import CaptureFixture, MonkeyPatch

from python.sets.check_subset import check_subset


class TestSubset:
    """Test cases for check_subset function"""

    def test_check_subset(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """check_subset is working as expected"""
        inputs = ["3", "5", "1 2 3 5 6", "9", "9 8 5 6 3 2 1 4 7", "1", "2", "5", "3 6 5 4 1", "7", "1 2 3 5 6 8 9", "3", "9 8 2"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        check_subset()
        captured = capsys.readouterr()
        assert captured.out == "True\nFalse\nFalse\n"

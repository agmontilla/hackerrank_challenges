""" Test Concatenate Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.concatenate import build_array, main, read_array


class TestConcatenate:
    """Test Concatenate Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = [
            "4 3 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "3 4",
            "3 4",
            "3 4",
        ]
        expected_outputs = "[[1 2]\n [1 2]\n [1 2]\n [1 2]\n [3 4]\n [3 4]\n [3 4]]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_build_array(self) -> None:
        """Test build_array function is working as expected"""
        arr = [["1", "2"], ["3", "4"]]
        expected = [[1, 2], [3, 4]]
        assert build_array(arr).tolist() == expected

    def test_read_array(self, monkeypatch: MonkeyPatch) -> None:
        """Test read_array function is working as expected"""
        rows = 2
        columns = 2
        inputs = ["1 2", "3 4"]
        expected = [["1", "2"], ["3", "4"]]
        monkeypatch = MonkeyPatch()
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        assert read_array(rows, columns) == expected

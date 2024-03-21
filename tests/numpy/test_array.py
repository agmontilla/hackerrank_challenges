"""Test Arrays Challenge"""

from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.array import arrays, main


class TestArrays:
    """Test Arrays Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = "1 2 3 4 -8 -10"
        expected_outputs = "[-10.  -8.   4.   3.   2.   1.]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs)
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_arrays(self) -> None:
        """Test arrays function is working as expected"""
        arr = ["1", "2", "3", "4", "-8", "-10"]
        expected = [-10.0, -8.0, 4.0, 3.0, 2.0, 1.0]
        assert arrays(arr).tolist() == expected

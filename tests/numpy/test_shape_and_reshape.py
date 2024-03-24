"""Test Shape and Reshape Challenge"""
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.shape_and_reshape import main, reshape_an_array


class TestShapeAndReshape:
    """Test Shape and Reshape Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = "1 2 3 4 5 6 7 8 9"
        expected_outputs = "[[1 2 3]\n [4 5 6]\n [7 8 9]]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs)
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_arrays(self) -> None:
        """Test arrays function is working as expected"""
        arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert reshape_an_array(arr).tolist() == expected

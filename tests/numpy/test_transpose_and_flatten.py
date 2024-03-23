"""" Test Cases for Transpose and Flatten Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.transpose_and_flatten import get_transpose_and_flatten, main


class TestTransposeAndFlatten:
    """Test Transpose and Flatten Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = [
            "2 2",
            "1 2",
            "3 4",
        ]
        expected_outputs = "[[1 3]\n [2 4]]\n[1 2 3 4]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_get_transpose_and_flatten(self) -> None:
        """Test get_transpose_and_flatten function is working as expected"""
        arr = [
            ["1", "2"],
            ["3", "4"],
        ]
        expected_transpose = [[1, 3], [2, 4]]
        expected_flatten = [1, 2, 3, 4]
        transpose, flatten = get_transpose_and_flatten(arr)
        assert transpose.tolist() == expected_transpose
        assert flatten.tolist() == expected_flatten

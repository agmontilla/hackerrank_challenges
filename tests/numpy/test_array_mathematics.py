import numpy as np
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.array_mathematics import apply_operations, main


class TestArrayMathematics:
    """Test Array Mathematics Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["1 4", "1 2 3 4", "5 6 7 8"]
        expected_output = "[[ 6  8 10 12]]\n[[-4 -4 -4 -4]]\n[[ 5 12 21 32]]\n[[0 0 0 0]]\n[[1 2 3 4]]\n[[    1    64  2187 65536]]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_apply_operations(self) -> None:
        """Test apply_operations function"""
        a = list(np.array([[1, 2, 3, 4]]))
        b = list(np.array([[5, 6, 7, 8]]))
        expected_output = [
            np.array([[6, 8, 10, 12]]),
            np.array([[-4, -4, -4, -4]]),
            np.array([[5, 12, 21, 32]]),
            np.array([[0, 0, 0, 0]]),
            np.array([[1, 2, 3, 4]]),
            np.array([[1, 64, 2187, 65536]]),
        ]

        results = apply_operations(a, b)

        for result, expected in zip(results, expected_output):
            assert np.array_equal(result, expected)

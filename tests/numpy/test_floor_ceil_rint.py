""" Test for Floor Ceil and Rint Challenge """
import numpy as np
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.floor_ceil_rint import apply_operations, main


class TestFloorCeilRint:
    """Test Floor Ceil and Rint Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"]
        expected_output = [
            "[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]",
            "[  2.   3.   4.   5.   6.   7.   8.   9.  10.]",
            "[  1.   2.   3.   4.   6.   7.   8.   9.  10.]",
        ]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        output = captured.out.splitlines()
        assert output == expected_output

    def test_apply_operations(self) -> None:
        """Test apply_operations function"""
        arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        expected_output = [
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
            [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            [1.0, 2.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10.0],
        ]

        results = apply_operations(arr)

        for result, expected in zip(results, expected_output):
            assert result.tolist() == expected

""" Tests for Inner and Outer challenge """
import numpy as np
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.inner_and_outer import apply_inner_outer, get_entries, main


class TestInnerOuter:
    """Inner and Outer Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["0 1", "2 3"]
        expected_output = "3\n[[0 0]\n [2 3]]\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_apply_inner_outer(self) -> None:
        """Test apply_inner_outer function"""
        expected_inner_output = 3
        expected_outer_output: np.ndarray = np.array([[0, 0], [2, 3]])
        a, b = [0, 1], [2, 3]
        inner_result, outer_result = apply_inner_outer(a, b)
        assert inner_result == expected_inner_output
        assert np.array_equal(outer_result, expected_outer_output)

    def test_get_entries(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_entries function"""
        input_values = ["1 2", "3 4"]
        expected_output = ([1, 2], [3, 4])
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        result = get_entries()
        assert result == expected_output

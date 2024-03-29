""" Tests for Mean, Var, and Std Challenge """
import numpy as np
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.mean_var_std import main, mean_var_std


class TestMeanVarStd:
    """Mean, Var, and Std Challenge"""

    def test_mean_var_std(self) -> None:
        """Test mean_var_std function"""
        data = [[1, 2], [3, 4]]
        mean, var, std = mean_var_std(data)
        assert all(np.equal(mean, np.array([1.5, 3.5])))
        assert all(np.equal(var, np.array([1.0, 1.0])))
        assert std == 1.11803398875

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2 2", "1 2", "3 4"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected_output = "[ 1.5  3.5]\n[ 1.  1.]\n1.11803398875\n"
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

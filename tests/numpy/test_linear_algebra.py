""" Test Linear Algebra Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.linear_algebra import calculate_det, get_entries, main


class TestLinearAlgebra:
    """Test Linear Algebra Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2", "1.1 1.1", "1.1 1.1"]
        expected_output = "0.0\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_calculate_det(self) -> None:
        """Test calculate_det function"""
        assert calculate_det([[1.1, 1.1], [1.1, 1.1]]) == 0.0

    def test_get_entries(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_entries function"""
        input_values = ["2", "1.1 1.1", "1.1 1.1"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        assert get_entries() == [[1.1, 1.1], [1.1, 1.1]]

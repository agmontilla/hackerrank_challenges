""" Test Polynomials Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.polynomials import apply_polynomial_operation, get_entries, main


class TestPolynomials:
    """Test Polynomials Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["1.1 2 3", "0"]
        expected_output = "3.0\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_apply_polynomial_operation(self) -> None:
        """Test apply_polynomial_operation function"""
        assert apply_polynomial_operation([1.1, 2, 3], 0) == 3.0

    def test_get_entries(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_entries function"""
        input_values = ["1.1 2 3", "0"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        assert get_entries() == ([1.1, 2, 3], 0)

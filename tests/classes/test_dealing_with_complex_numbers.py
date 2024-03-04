""" Test Dealing with Complex Numbers Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.classes.dealing_with_complex_numbers import Complex, main


class TestDealingWithComplexNumbers:
    """Test Dealing with Complex Numbers module"""

    def test_add_operation(self) -> None:
        """Test add operation using Complex numbers"""
        c = Complex(2, 1)
        d = Complex(5, 6)
        result = c + d
        assert result.real == 7
        assert result.imaginary == 7

    def test_sub_operation(self) -> None:
        """Test sub operation using Complex numbers"""
        c = Complex(2, 1)
        d = Complex(5, 6)
        result = c - d
        assert result.real == -3
        assert result.imaginary == -5

    def test_mul_operation(self) -> None:
        """Test mul operation using Complex numbers"""
        c = Complex(2, 1)
        d = Complex(5, 6)
        result = c * d
        assert result.real == 4
        assert result.imaginary == 17

    def test_truediv_operation(self) -> None:
        """Test truediv operation using Complex numbers"""
        c = Complex(2, 1)
        d = Complex(5, 6)
        result = c / d
        assert result.real == 0.26229508196721313
        assert result.imaginary == -0.11475409836065574

    def test_mod_operation(self) -> None:
        """Test mod operation using Complex numbers"""
        c = Complex(2, 1)
        result = c.mod()
        assert result.real == 2.23606797749979
        assert result.imaginary == 0

    def test_str_operation(self) -> None:
        """Test str operation using Complex numbers"""
        c = Complex(2, 1)
        result = str(c)
        assert result == "2.00+1.00i"

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2 1", "5 6"]
        output_value = "7.00+7.00i\n-3.00-5.00i\n4.00+17.00i\n0.26-0.11i\n2.24+0.00i\n7.81+0.00i\n"

        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == output_value

""" Test for Sum and Prod Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.sum_and_prod import main, perform_operations


class TestSumAndProd:
    """Test Sum and Prod Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2 2", "1 2", "3 4"]
        expected_output = "24\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_perform_operations(self) -> None:
        """Test perform_operations function"""
        data = [[1, 2], [3, 4]]
        expected_output = 24

        result = perform_operations(data)
        assert result == expected_output

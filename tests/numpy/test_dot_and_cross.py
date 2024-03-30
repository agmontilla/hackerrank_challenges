""" Test Dot and Cross Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.dot_and_cross import apply_dot_operation, get_entries, main


class TestDotAndCross:
    """Test Dot and Cross Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["2", "1 2", "3 4", "1 2", "3 4"]
        expected_output = "[[ 7 10]\n [15 22]]\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_get_entries(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_entries function"""
        input_values = ["2", "1 2", "3 4", "1 2", "3 4"]
        expected_output = ([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        assert get_entries() == expected_output

    def test_apply_dot_operation(self) -> None:
        """Test apply_dot_operation function"""
        a, b = [[1, 2], [3, 4]], [[1, 2], [3, 4]]
        expected_output = [[7, 10], [15, 22]]
        assert apply_dot_operation(a, b).tolist() == expected_output

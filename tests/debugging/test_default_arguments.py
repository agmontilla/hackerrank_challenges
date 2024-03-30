""" Test Default Arguments Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.debugging.default_arguments import OddStream, main, print_from_stream


class TestDefaultArguments:
    """Test Default Arguments Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["3", "odd 2", "even 3", "odd 5"]
        expected_output = "1\n3\n0\n2\n4\n1\n3\n5\n7\n9\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_print_from_stream_when_stream_is_even(self, capsys: CaptureFixture) -> None:
        """Test print_from_stream function"""
        print_from_stream(3)
        captured = capsys.readouterr()
        assert captured.out == "0\n2\n4\n"

    def test_print_from_stream_when_stream_is_odd(self, capsys: CaptureFixture) -> None:
        """Test print_from_stream function"""
        print_from_stream(3, OddStream())
        captured = capsys.readouterr()
        assert captured.out == "1\n3\n5\n"

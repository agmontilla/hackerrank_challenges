""" Test Split Challenge """

from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.split import main


class TestSplit:
    """Test Split module."""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function."""
        inputs = ["100,000,000.000"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        output = "100\n000\n000\n000\n"

        main()
        captured = capsys.readouterr()
        assert captured.out == output

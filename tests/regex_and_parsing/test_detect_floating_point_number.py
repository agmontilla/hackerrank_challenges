""" Test Detect Floating Point Number Challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.regex_and_parsing.detect_floating_point_number import is_float, main


class TestDetectFloatingPointNumber:
    """Test Detect Floating Point Number module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function."""
        inputs = ["4", "4.0O0", "-1.00", "+4.54", "SomeRandomStuff"]
        outputs = "False\nTrue\nTrue\nFalse\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == outputs

    @mark.parametrize(
        "input_, expected",
        [
            ("4.0O0", False),
            ("-1.00", True),
            ("+4.54", True),
            ("SomeRandomStuff", False),
        ],
    )
    def test_float(self, input_: str, expected: bool) -> None:
        """Test is_float function."""
        assert is_float(input_) is expected

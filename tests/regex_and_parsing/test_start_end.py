""" Test StartEnd class """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.regex_and_parsing.start_end import StartEnd, main


class TestStartEnd:
    """StartEnd test class"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test run function"""
        inputs = ["aaadaa", "aa"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "(0, 1)\n(1, 2)\n(4, 5)\n"

    @mark.parametrize(
        "sentence, k, expected",
        [("aaadaa", "aa", ["(0, 1)", "(1, 2)", "(4, 5)"]), ("aaadaa", "b", ["(-1, -1)"])],
    )
    def test_get_indexes(self, sentence: str, k: str, expected: list[str]) -> None:
        """Test run function"""
        start_end = StartEnd(sentence, k)
        result = start_end.get_indexes()
        assert result == expected

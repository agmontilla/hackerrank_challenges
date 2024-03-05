""" Test Ginorts challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.built_ins.ginorts import InverseSort, main


class TestGinorts:
    """Test Ginorts challenge"""

    @mark.parametrize(
        "sentence, expected",
        [
            ("Sorting1234", "ginortS1324"),
            (
                "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPLKJHGFDSAZXCVBNM",
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468",
            ),
        ],
    )
    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch, sentence: str, expected: str) -> None:
        """Test main function"""
        monkeypatch.setattr("builtins.input", lambda: sentence)
        main()
        captured = capsys.readouterr()
        assert captured.out == f"{expected}\n"

    @mark.parametrize(
        "sentence, expected",
        [
            ("Sorting1234", "ginortS1324"),
            (
                "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPLKJHGFDSAZXCVBNM",
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468",
            ),
        ],
    )
    def test_custom_sorted(self, sentence: str, expected: str) -> None:
        """Test custom_sorted method"""
        expression = InverseSort(sentence)
        assert expression.custom_sorted() == expected

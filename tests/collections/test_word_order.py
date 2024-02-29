""" Test cases for Word Order Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.word_order import get_counting_words, main


class TestWordOrder:
    """Test Word Order module"""

    def test_get_counting_words(self) -> None:
        """Test get_counting_words function is working as expected"""
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        expected = {"bcdef": 2, "abcdefg": 1, "bcde": 1}
        assert get_counting_words(words) == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = ["4", "bcdef", "abcdefg", "bcde", "bcdef"]
        output = "3\n2 1 1\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == output

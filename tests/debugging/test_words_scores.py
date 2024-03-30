""" Words Scores Challenge Tests """
import pytest

from challenges.debugging.words_scores import is_vowel, score_words


class TestWordsScores:
    """Test Words Scores Challenge"""

    def test_is_vowel(self) -> None:
        """Test is_vowel function"""
        assert is_vowel("a") is True
        assert is_vowel("b") is False

    @pytest.mark.parametrize(
        "words, expected",
        [
            (["programming", "is", "awesome"], 4),
            (["hacker", "book"], 4),
        ],
    )
    def test_score_words(self, words: list[str], expected: int) -> None:
        """Test score_words function"""
        assert score_words(words) == expected

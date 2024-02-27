""" Tests for Iterable and Iterators challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.iterable_and_iterators import find_probability, main


class TestIterableAndIterators:
    """Tests for Iterable and Iterators challenge."""

    def test_find_probability(self) -> None:
        """Should return the probability of the combination with the letter 'a'."""
        s = ["a", "a", "c", "d"]
        k = 2
        expected = 0.8333333333333334

        result = find_probability(s, k)

        assert result == expected

    def test_iterable_and_iterator_main_program(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Should print the probability of the combination."""
        inputs = ["4", "a a c d", "2"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()

        captured = capsys.readouterr()
        output = "0.8333\n"
        assert captured.out == output

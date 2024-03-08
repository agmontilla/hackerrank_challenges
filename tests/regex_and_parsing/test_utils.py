""" Test utils module """

from pytest import MonkeyPatch, raises

from challenges.regex_and_parsing.utils import Reader


class TestReader:
    """Test Reader class"""

    def test_readlines(self, monkeypatch: MonkeyPatch) -> None:
        """Test readlines method"""
        inputs = ["3", "1", "2", "3"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        reader = Reader()

        lines = reader.readlines()

        assert lines == ["1", "2", "3"]

    def test_readlines_with_big_number_of_lines(self, monkeypatch: MonkeyPatch) -> None:
        """Test readlines method with big number of lines"""
        inputs = ["101"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        reader = Reader()

        with raises(ValueError) as exc:
            reader.readlines()
        assert str(exc.value) == "Number of lines is too big"

""" Test utils module """

from pytest import MonkeyPatch, raises

from challenges.regex_and_parsing.utils import MatrixReader, Reader


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


class TestMatrixReader:
    """Test MatrixReader class"""

    def test_readlines(self, monkeypatch: MonkeyPatch) -> None:
        """Test readlines method"""
        inputs = ["3 3", "1 2 3", "4 5 6", "7 8 9"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        reader = MatrixReader()

        lines = reader.readlines()

        assert lines == ["1 2 3", "4 5 6", "7 8 9"]

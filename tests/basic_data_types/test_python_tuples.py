"""Test cases for the Python Tuples challenge."""
from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.python_tuples import get_hash, main


class TestPythonTuples:
    """Test for the Python Tuples challenge."""

    def test_get_hash_is_working(self) -> None:
        """Test for the get_hash function is working as expected."""
        assert get_hash((1, 2)) == -3550055125485641917

    def test_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected.

        Note: this expected value differs from the original one because the hash function is not deterministic.
        to get more info about it, please check
        https://stackoverflow.com/questions/68524748/hashing-a-tuple-not-matching-the-expected-value-in-python
        """

        input_values = [
            "2",
            "1 2",
        ]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected = "-3550055125485641917\n"

        main()

        out, _ = capsys.readouterr()
        assert out == expected

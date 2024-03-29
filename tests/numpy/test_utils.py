""" Tests for numpy utils module """
from pytest import MonkeyPatch

from challenges.numpy.utils import get_entries


class Utils:
    """Test for numpy utils module"""

    def test_get_entries(self, monkeypatch: MonkeyPatch) -> None:
        """Test get_entries function"""
        input_values = ["2 2", "1 2", "3 4"]
        expected_output = [[1, 2], [3, 4]]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        result = get_entries()
        assert result == expected_output

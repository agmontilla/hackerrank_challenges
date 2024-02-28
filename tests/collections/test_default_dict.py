""" Test DefaultDict challenge """

from collections import defaultdict
from typing import DefaultDict

from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.default_dict import main, total_per_letter


class TestDefaultDict:
    """Test DefaultDict module"""

    def test_total_per_letter(self, monkeypatch: MonkeyPatch) -> None:
        """Test total_per_letter function is working as expected"""
        # Arrange
        input_values = ["a", "a", "b", "a", "b", "a", "b"]
        expected_output = ["1 2 4", "3 5"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        all_positions: DefaultDict = defaultdict(lambda: -1)

        # Act
        results = total_per_letter(5, 2, all_positions)

        # Assert
        assert results == expected_output

    def test_default_dict_main_program(self, monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
        """Test the main program"""
        # Arrange
        input_values = ["5 2", "a", "a", "b", "a", "b", "a", "b", "a", "b"]
        expected_output = "1 2 4\n3 5\n"
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        # Act
        main()

        # Assert
        captured = capsys.readouterr()
        assert captured.out == expected_output

""" Test Counter Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.counter import get_profits, main


class TestCounter:
    """Test Counter module"""

    def test_get_profits(self) -> None:
        """Test get_profits is working as expected"""
        results = get_profits([2, 3, 4, 5, 6, 8, 7, 6, 5, 18], [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)])
        assert results == 200

    def test_counter_main_program(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main program"""
        # Arrange
        input_values = ["10", "2 3 4 5 6 8 7 6 5 18", "6", "6 55", "6 45", "6 55", "4 40", "18 60", "10 50"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        # Act
        main()
        captured = capsys.readouterr()

        # Assert
        assert captured.out == "200\n"

""" Test cases for the minion game """
from pytest import CaptureFixture

from python.strings.the_minion_game import minion_game


class TestMinionGame:
    """Test cases for the minion_game function"""

    def test_minion_game_is_working(self, capsys: CaptureFixture) -> None:
        """minion_game is working as expected"""
        # Arrange
        string = "BANANA"
        expected = "Stuart 12\n"

        # Act
        minion_game(string)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected

from python.strings.the_minion_game import minion_game
from pytest import CaptureFixture


class TestMinionGame():

    def test_minion_game_is_working(self, capsys: CaptureFixture) -> None:
        # Arrange
        string = 'BANANA'
        expected = 'Stuart 12\n'

        # Act
        minion_game(string)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected

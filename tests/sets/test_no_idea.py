""" Test cases for No Idea!"""

from pytest import CaptureFixture, MonkeyPatch

from challenges.sets.no_idea import calculate_happines, main


class TestHappines:
    """Test calculate happines"""

    def test_calculate_happines_is_working(self) -> None:
        """Calculate happines is working as expected"""
        # Arrange
        arr = [1, 5, 3]
        set_a = {3, 1}
        set_b = {5, 7}

        # Act
        result = calculate_happines(arr, set_a, set_b)

        # Assert
        assert result == 1

    def test_happines_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Main program is working as expected"""
        # Arrange
        user_input = ["3 2", "1 5 3", "3 1", "5 7"]
        expected_output = "1\n"
        monkeypatch.setattr("builtins.input", lambda: user_input.pop(0))

        # Act
        main()
        captured = capsys.readouterr()

        # Assert
        assert captured.out == expected_output

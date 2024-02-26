""" Tests for the second max number in a list challenge. """

from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.find_second_max_number_in_a_list import (
    get_runner_up,
    main,
)


class TestFindSecondMaxNumberInAList:
    """Tests for the second max number in a list challenge."""

    def test_get_runner_up_is_working(self) -> None:
        """Test get_runner_up function is working as expected"""
        result = get_runner_up(5, [2, 3, 6, 6, 5])
        assert result == 5

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""

        # Arrange
        input_values = ["5", "2 3 6 6 5"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        # Act
        main()
        captured = capsys.readouterr()

        # Assert
        assert captured.out == "5\n"

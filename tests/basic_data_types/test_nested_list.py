""" Tests for the Nested List challenge. """
from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.nested_list import get_second_lowest_grade, main


class TestNestedList:
    """Test for the Nested List challenge."""

    def test_get_second_lowest_grade(self) -> None:
        """Test for the function get_second_lowest_grade is working as expected."""
        data = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]
        expected = ["Berry", "Harry"]

        results = get_second_lowest_grade(data)

        assert results == expected

    def test_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected."""

        input_values = ["5", "Harry", "37.21", "Berry", "37.21", "Tina", "37.2", "Akriti", "41", "Harsh", "39"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected = "Berry\nHarry\n"

        main()

        out, _ = capsys.readouterr()
        assert out == expected

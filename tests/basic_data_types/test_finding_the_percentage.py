""" Test for the percentage challenge. """

from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.finding_the_percentage import main, percentage


class TestFindingPercentage:
    """Test for the function percentage."""

    def test_percentage_is_working(self) -> None:
        """Test for the function percentage is working as expected."""
        student_marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
        query_name = "Malika"
        assert percentage(student_marks, query_name) == "56.00"

    def test_percentage_is_working_with_empty_dict(self) -> None:
        """Test for the function percentage is working as expected."""
        student_marks: dict = {}
        query_name = "Malika"
        assert percentage(student_marks, query_name) == "0.00"

    def test_percentage_is_working_with_name_not_in_dict(self) -> None:
        """Test for the function percentage is working as expected."""
        student_marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
        query_name = "Kartik"
        assert percentage(student_marks, query_name) == "0.00"

    def test_finding_percentage_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected."""

        input_values = ["3", "Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60", "Malika"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()

        out, _ = capsys.readouterr()
        assert out == "56.00\n"

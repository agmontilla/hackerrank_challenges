""" Test cases for calendar challenge """

from pytest import CaptureFixture, MonkeyPatch

from challenges.date_and_time.calendar_module import get_day_name, main


class TestCalendarModule:
    """Test cases for calendar module"""

    def test_get_day_name(self) -> None:
        """Check if get_day_name function is working as expected."""
        assert get_day_name(2015, 8, 5) == "WEDNESDAY"

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Check if main function is working as expected."""
        inputs = ["08 05 2015"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "WEDNESDAY\n"

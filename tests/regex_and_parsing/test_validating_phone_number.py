"""" Tests for the validating phone number problem challenge """

from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.validating_phone_number import PhoneNumbers, main


class TestValidatingPhoneNumber:
    """Tests for the validating phone number problem module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["2", "9587456281", "1252478965"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "YES\nNO\n"

    def test_are_valid(self) -> None:
        """Test are_valid method"""
        phone_numbers = ["9587456281", "1252478965"]
        assert PhoneNumbers(phone_numbers).are_valid() == ["YES", "NO"]

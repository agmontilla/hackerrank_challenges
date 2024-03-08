""" Test Validating Email Address Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.validating_named_email_address import Users, main


class TestValidatingEmailAddress:
    """Test Validating Email Address module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["2", "DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>"]
        output = "DEXTER <dexter@hotmail.com>\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()

        captured = capsys.readouterr()
        assert captured.out == output

    def test_get_valid_email_addresses(self) -> None:
        """Test get_valid_email_addresses method"""
        users = Users([("DEXTER", "dexter@hotmail.com"), ("VIRUS", "virus!@variable.:p")])
        assert list(users.get_valid_email_addresses()) == ["DEXTER <dexter@hotmail.com>"]

""" Test Group(), Groups() & Groupdict() Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.group_groups_groupdict import main


class TestGroupGroupsGroupdict:
    """Test Group(), Groups() & Groupdict() module."""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function."""
        inputs = ["12345678910111213141516171820212223"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        output = "1\n"

        main()
        captured = capsys.readouterr()
        assert captured.out == output

""" Test Company Logo Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.company_logo import main, most_common


class TestCompanyLogo:
    """Test Company Logo module"""

    def test_most_common(self) -> None:
        """Most_common function is working as expecected"""
        assert most_common("aabbbccde") == {"a": 2, "b": 3, "c": 2, "d": 1, "e": 1}

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Should print the most common letters"""
        inputs = ["aabbbccde"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "b 3\na 2\nc 2\n"

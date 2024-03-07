""" Test FindAll and FindIter Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.findall_finditer import FindVowels, main


class TestFindAllFindIter:
    """Test FindAll and FindIter module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["rabcdeefgyYhFjkIoomnpOeorteeeeet"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "ee\nIoo\nOeo\neeeee\n"

    def test_consonants(self) -> None:
        """Test get_consonants"""
        assert FindVowels.CONSONANT == "bcdfghjklmnpqrstvwxyz"

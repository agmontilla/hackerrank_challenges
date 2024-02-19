""" Tests for the add function in the sets module. """
from pytest import CaptureFixture, MonkeyPatch

from python.sets.add import add


class TestAdd():
    """ Test cases for add function """

    def test_add_is_working_as_expected(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """ add is working as expected """
        inputs = ["UK", "China", "USA", "France",
                  "New Zealand", "UK", "France", "UK"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        add(7)
        captured = capsys.readouterr()
        assert captured.out == "5\n"

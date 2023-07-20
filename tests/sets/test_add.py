
from pytest import CaptureFixture, MonkeyPatch
from python.sets.add import add


class TestAdd():

    def test_add_is_working_as_expected(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        inputs = ["UK", "China", "USA", "France", "New Zealand", "UK", "France", "UK"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        add(7)
        captured = capsys.readouterr()
        assert captured.out == "5\n"

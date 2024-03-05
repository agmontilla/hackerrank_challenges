""" Test Python Evaluation Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.built_ins.python_evaluation import main


class TestPythonEvaluation:
    """Test Python Evaluation module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["print(2 + 3)"]
        output = "5\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == output

""" Test for Map and Lambda Function Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.functionals.map_and_lambda import fibonacci, main


class TestMapAndLambda:
    """Test Map and Lambda Function module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        monkeypatch.setattr("builtins.input", lambda: "5")
        main()
        captured = capsys.readouterr()
        assert captured.out == "[0, 1, 1, 8, 27]\n"

    def test_fibonacci(self) -> None:
        """Test fibonacci function"""
        assert not fibonacci(0)
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

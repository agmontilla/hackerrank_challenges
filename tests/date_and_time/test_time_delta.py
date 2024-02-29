"""Test time_delta challenge"""
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.date_and_time.time_delta import main, time_delta


class TestTimeDelta:
    """Test time_delta module"""

    @mark.parametrize(
        "t1, t2, expected",
        [
            ("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000", "25200"),
            ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000", "88200"),
        ],
    )
    def test_time_delta(self, t1: str, t2: str, expected: str) -> None:
        """Test time_delta function"""
        assert time_delta(t1, t2) == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = [
            "2",
            "Sun 10 May 2015 13:54:36 -0700",
            "Sun 10 May 2015 13:54:36 -0000",
            "Sat 02 May 2015 19:54:36 +0530",
            "Fri 01 May 2015 13:54:36 -0000",
        ]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "25200\n88200\n"

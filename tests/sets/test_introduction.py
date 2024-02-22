""" Test for set introduction module """

from pytest import CaptureFixture, MonkeyPatch

from python.sets.introduction import average, main


class TestSetIntroduction:
    """ Test for set introduction module """

    def test_set_introduction(self) -> None:
        """ average function is working as expected"""
        assert average(
            [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]) == 169.375

    def test_main_introduction_program(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """ main function is working as expected """
        inputs = ["10", "161 182 161 154 176 170 167 171 170 174"]
        monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == '169.375\n'

from python.strings.string_formatting import print_formatted

from pytest import CaptureFixture


class TestPrintFormatting():

    def test_print_formatting_is_working(self, capsys: CaptureFixture) -> None:
        print_formatted(2)
        captured = capsys.readouterr()
        assert captured.out == ' 1  1  1  1\n 2  2  2 10\n'

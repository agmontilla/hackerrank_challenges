from python.strings.alphabet_rangoli import print_rangoli

from pytest import CaptureFixture


class TestAlphabetRangoli():

    def test_alphabet_rangoli_is_working(self, capfd: CaptureFixture) -> None:

        expected = '----c----\n--c-b-c--\nc-b-a-b-c\n--c-b-c--\n----c----\n'
        print_rangoli(3)
        out, _ = capfd.readouterr()
        assert out == expected

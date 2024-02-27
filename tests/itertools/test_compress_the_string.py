""" Test cases for Compress the String! Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.itertools.compress_the_string import compress_the_string, main


class TestCompressTheString:
    """Test for Compress the String! Challenge"""

    def test_compress_the_string(self) -> None:
        """Test compress_the_string function is working as expected."""
        expected = [(1, 1), (3, 2), (1, 3), (2, 1)]
        results = compress_the_string("1222311")
        assert results == expected

    def test_compress_the_string_main_program(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected."""
        expected = "(1, 1) (3, 2) (1, 3) (2, 1)\n"
        monkeypatch.setattr("builtins.input", lambda: "1222311")
        main()
        out, _ = capsys.readouterr()
        assert out == expected

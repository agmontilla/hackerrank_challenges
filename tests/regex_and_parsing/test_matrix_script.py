""" Test for MatrixScript """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.matrix_script import MatrixScript, main


class TestMatrixScript:
    """Test cases for MatrixScript class"""

    def test_main(self, monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
        """Test main function"""
        inputs = ["7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "This is Matrix#  %!"

    def test_decode_message(self) -> None:
        """Get message from matrix is working as expected"""
        matrix = [
            "Tsi",
            "h%x",
            "i #",
            "sM ",
            "$a ",
            "#t%",
            "ir!",
        ]
        ms = MatrixScript(matrix)
        assert ms.get_message() == "This is Matrix#  %!"

    def test_decode_message_2(self) -> None:
        """Get a complex message from matrix is working as expected"""
        matrix = [
            "r F",
            "w  ",
            "  e",
            "h  ",
            "si ",
            " $ ",
            "#rt",
            "a G",
            "!e ",
            "t# ",
            "i p",
            "t  ",
        ]
        ms = MatrixScript(matrix)
        assert ms.get_message() == "rw hs a tit i r e F e tG p "

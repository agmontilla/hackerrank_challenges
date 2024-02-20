""" Test for MatrixScript """
from python.regex_and_parsing.matrix_script import MatrixScript


class TestMatrixScript:
    """ Test cases for MatrixScript class """

    def test_decode_message(self) -> None:
        """ Get message from matrix is working as expected """
        matrix = [
            'Tsi',
            'h%x',
            'i #',
            'sM ',
            '$a ',
            '#t%',
            'ir!',
        ]
        ms = MatrixScript(matrix)
        assert ms.get_message() == 'This is Matrix#  %!'

    def test_decode_message_2(self) -> None:
        """ Get a complex message from matrix is working as expected """
        matrix = [
            'r F',
            'w  ',
            '  e',
            'h  ',
            'si ',
            ' $ ',
            '#rt',
            'a G',
            '!e ',
            't# ',
            'i p',
            't  ',
        ]
        ms = MatrixScript(matrix)
        assert ms.get_message() == 'rw hs a tit i r e F e tG p '

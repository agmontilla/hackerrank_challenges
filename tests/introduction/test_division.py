""" Tests for the Division challenge """

from pytest import CaptureFixture

from challenges.introduction.division import main


class TestDivision:
    """Tests for the Division challenge"""

    def test_division_main_program_is_working(self, capsys: CaptureFixture) -> None:
        """Test the main program of division is working as expected"""
        main(4, 3)
        captured = capsys.readouterr()
        assert captured.out == "1\n1.3333333333333333\n"

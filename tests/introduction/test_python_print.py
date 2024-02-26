""" Tests for the Python Print challenge """

from pytest import CaptureFixture

from challenges.introduction.python_print import print_str


class TestPrintStr:
    """Tests for the Print Str challenge"""

    def test_print_str(self, capsys: CaptureFixture) -> None:
        """Test print_str is working as expected"""
        expected_output = "12345"

        print_str(5)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

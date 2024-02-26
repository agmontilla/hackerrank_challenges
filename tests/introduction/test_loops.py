""" Tests for the Loops challenge """

from pytest import CaptureFixture

from challenges.introduction.loops import square


class TestLoops:
    """Tests for the Loops challenge"""

    def test_square(self, capsys: CaptureFixture) -> None:
        """Test square is working as expected"""
        expected_output = "0\n1\n4\n9\n16"

        square(5)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

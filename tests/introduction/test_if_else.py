""" Tests for the If-Else challenge """

from pytest import CaptureFixture

from challenges.introduction.if_else import main


class TestIfElse:
    """Tests for the If-Else challenge"""

    def test_odd_number(self, capsys: CaptureFixture) -> None:
        """Test odd number is working as expected"""
        expected_output = "Weird"

        main(3)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

    def test_even_number_in_range_2_to_5(self, capsys: CaptureFixture) -> None:
        """Test even number in range 2 to 5 is working as expected"""
        expected_output = "Not Weird"

        main(4)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

    def test_even_number_in_range_6_to_20(self, capsys: CaptureFixture) -> None:
        """Test even number in range 6 to 20 is working as expected"""
        expected_output = "Weird"

        main(20)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

    def test_even_number_greater_than_20(self, capsys: CaptureFixture) -> None:
        """Test even number greater than 20 is working as expected"""
        expected_output = "Not Weird"

        main(24)
        out, _ = capsys.readouterr()

        assert out.strip() == expected_output

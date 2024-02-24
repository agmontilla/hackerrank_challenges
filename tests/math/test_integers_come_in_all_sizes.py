""" Test cases for IntegersComeInAllSizes module. """
from pytest import CaptureFixture

from challenges.math.integers_come_in_all_sizes import IntegersComeInAllSizes


class TestIntegersComeInAllSizes:
    """Test cases for IntegersComeInAllSizes class"""

    def test_integers_come_in_all_sizes_1(self, capfd: CaptureFixture) -> None:
        """IntegersComeInAllSizes is working as expected"""
        output = ["4710194409608608369201743232"]
        expected = "\n".join(output) + "\n"

        IntegersComeInAllSizes.get_integers_come_in_all_sizes(9, 29, 7, 27)
        out, _ = capfd.readouterr()
        assert out == expected

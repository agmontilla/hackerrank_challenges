""" Test cases for the TriangleQuest2 module. """
from pytest import CaptureFixture

from python.math.triangle_quest2 import TriangleQuest2


class TestTriangleQuest2:
    """Test cases for TriangleQuest2 class"""

    def test_triangle_quest2_1(self, capfd: CaptureFixture) -> None:
        """TriangleQuest2 is working as expected"""
        output = ["1", "121", "12321", "1234321", "123454321"]
        expected = "\n".join(output) + "\n"

        TriangleQuest2.get_triangle_quest2(5)
        out, _ = capfd.readouterr()
        assert out == expected

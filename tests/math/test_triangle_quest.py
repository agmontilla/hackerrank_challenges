""" Test cases for the Triangle Quest problem. """
from pytest import CaptureFixture

from challenges.math.triangle_quest import TriangleQuest


class TestTriangleQuest:
    """Test cases for TriangleQuest class"""

    def test_triangle_quest_1(self, capfd: CaptureFixture) -> None:
        """TriangleQuest is working as expected"""
        output = ["1", "22", "333", "4444"]
        expected = "\n".join(output) + "\n"

        TriangleQuest.triangle_quest(5)
        out, _ = capfd.readouterr()
        assert out == expected

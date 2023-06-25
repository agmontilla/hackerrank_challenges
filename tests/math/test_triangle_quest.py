
from python.math.triangle_quest import TriangleQuest
from pytest import CaptureFixture


class TestTriangleQuest():

    def test_triangle_quest_1(self, capfd: CaptureFixture) -> None:

        output = ["1", "22", "333", "4444"]
        expected = "\n".join(output) + "\n"

        TriangleQuest.triangle_quest(5)
        out, _ = capfd.readouterr()
        assert out == expected

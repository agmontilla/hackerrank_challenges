from python.math.triangle_quest2 import TriangleQuest2
from pytest import CaptureFixture


class TestTriangleQuest2():

    def test_triangle_quest2_1(self, capfd: CaptureFixture) -> None:

        output = ["1", "121", "12321", "1234321", "123454321"]
        expected = "\n".join(output) + "\n"

        TriangleQuest2.get_triangle_quest2(5)
        out, _ = capfd.readouterr()
        assert out == expected

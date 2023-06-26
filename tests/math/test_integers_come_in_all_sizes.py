from python.math.integers_come_in_all_sizes import IntegersComeInAllSizes
from pytest import CaptureFixture


class TestIntegersComeInAllSizes():
    def test_integers_come_in_all_sizes_1(self, capfd: CaptureFixture) -> None:
        output = ["4710194409608608369201743232"]
        expected = "\n".join(output) + "\n"

        IntegersComeInAllSizes.get_integers_come_in_all_sizes(9, 29, 7, 27)
        out, _ = capfd.readouterr()
        assert out == expected
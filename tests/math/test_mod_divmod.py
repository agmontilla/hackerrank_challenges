from pytest import CaptureFixture
from python.math.mod_divmod import ModDivmod


class TestModDivmod(object):

    def test_mod(self, capfd: CaptureFixture) -> None:
        ModDivmod.get_mod_divmod(177, 10)
        out, _ = capfd.readouterr()
        assert out == "17\n7\n(17, 7)\n"

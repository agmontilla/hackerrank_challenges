
from python.math.power_modpower import PowerModPower
from pytest import CaptureFixture


class TestModPower():

    def test_mod_power_1(self, capfd: CaptureFixture) -> None:
        PowerModPower.get_power_modpower(3, 4, 5)
        out, _ = capfd.readouterr()
        assert out == "81\n1\n"

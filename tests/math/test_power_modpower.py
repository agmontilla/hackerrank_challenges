""" Test for PowerModPower class """
from pytest import CaptureFixture

from python.math.power_modpower import PowerModPower


class TestModPower:
    """Test cases for PowerModPower class"""

    def test_mod_power_1(self, capfd: CaptureFixture) -> None:
        """PowerModPower is working as expected"""
        PowerModPower.get_power_modpower(3, 4, 5)
        out, _ = capfd.readouterr()
        assert out == "81\n1\n"

""" Test cases for the ModDivmod class. """
from pytest import CaptureFixture

from challenges.math.mod_divmod import ModDivmod


class TestModDivmod:
    """Test cases for ModDivmod class"""

    def test_mod(self, capfd: CaptureFixture) -> None:
        """ModDivmod is working as expected"""
        ModDivmod.get_mod_divmod(177, 10)
        out, _ = capfd.readouterr()
        assert out == "17\n7\n(17, 7)\n"

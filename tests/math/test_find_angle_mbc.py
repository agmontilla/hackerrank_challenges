""" Test cases for find_angle_mbc.py """

from python.math.find_angle_mbc import AngleMBC


class TestAngleMBC:
    """Test cases for AngleMBC class"""

    def test_angle_mbc_is_working(self) -> None:
        """Angle MBC is working as expected"""
        ab, bc = 10, 10
        angle_mbc = AngleMBC(ab, bc)
        assert str(angle_mbc) == "45°"

    def test_angle_mbc_is_truncating_values_as_expected(self) -> None:
        """Angle MBC is truncating values as expected"""
        ab, bc = 56, 10
        angle_mbc = AngleMBC(ab, bc)
        assert str(angle_mbc) == "80°"

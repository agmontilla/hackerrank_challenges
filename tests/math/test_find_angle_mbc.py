from python.math.find_angle_mbc import AngleMBC


class TestAngleMBC():

    def test_angle_mbc_is_working(self) -> None:
        ab, bc = 10, 10
        angle_mbc = AngleMBC(ab, bc)
        assert str(angle_mbc) == '45°'

    def test_angle_mbc_is_truncating_values_as_expected(self) -> None:
        ab, bc = 56, 10
        angle_mbc = AngleMBC(ab, bc)
        assert str(angle_mbc) == '80°'

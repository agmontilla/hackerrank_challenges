""" Test for designer_door_mat.py """
import pytest
from pytest import CaptureFixture

from python.strings.designer_door_mat import check_columns, is_odd, print_dot


class TestDesignerDoorMat:
    """Test cases for the designer_door_mat functions"""

    def test_designer_door_mat_is_working(self, capfd: CaptureFixture) -> None:
        """Test if designer_door_mat is working as expected"""
        expected = (
            "------------.|.------------\n"
            "---------.|..|..|.---------\n"
            "------.|..|..|..|..|.------\n"
            "---.|..|..|..|..|..|..|.---\n"
            "----------WELCOME----------\n"
            "---.|..|..|..|..|..|..|.---\n"
            "------.|..|..|..|..|.------\n"
            "---------.|..|..|.---------\n"
            "------------.|.------------\n"
        )

        print_dot(9, 27)

        out, _ = capfd.readouterr()
        assert out == expected

    def test_is_odd_is_working(self) -> None:
        """Test if is_odd is working as expected"""
        assert is_odd(3)
        with pytest.raises(ValueError):
            is_odd(4)

    def test_check_columns_is_working(self) -> None:
        """Test if check_columns is working as expected"""
        assert check_columns(3, 9)
        with pytest.raises(ValueError):
            check_columns(3, 10)

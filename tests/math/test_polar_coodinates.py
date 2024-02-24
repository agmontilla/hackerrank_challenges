""" Test Cases for Polar Coordinates Class """

from challenges.math.polar_coordinates import PolarCoordinates


class TestPolarCoordinates:
    """Test Class for Polar Coordinates Class"""

    def test_str_representation_is_working(self) -> None:
        """Test __str__ representation is working as expected"""
        complex_number = "1+2j"
        expected = "2.23606797749979\n1.1071487177940904"
        polar_coordinates = PolarCoordinates(complex_number)
        assert str(polar_coordinates) == expected

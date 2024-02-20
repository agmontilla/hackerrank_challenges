""" Polar Coordinates """
from cmath import phase
from math import sqrt


class PolarCoordinates():
    """ Polar Coordinates Class """

    def __init__(self, complex_number: str) -> None:
        self.complex_number = complex(complex_number)

    def __str__(self) -> str:
        """ Returns the polar coordinates of a complex number """
        return f'{sqrt(self.complex_number.real**2+self.complex_number.imag**2)}\n{phase(self.complex_number)}'


def main() -> None:
    """ Main function """
    complex_number = input()
    polar_coordinates = PolarCoordinates(complex_number)
    print(polar_coordinates)


if __name__ == "__main__":
    main()

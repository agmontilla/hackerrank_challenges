""" Dealing with Complex Numbers Challenge """

import math


class Complex(object):
    """Class to save a complex number and perform operations with it"""

    def __init__(self, real: float, imaginary: float):
        self.real, self.imaginary = real, imaginary

    def __add__(self, no: "Complex") -> "Complex":
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no: "Complex") -> "Complex":
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no: "Complex") -> "Complex":
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no: "Complex") -> "Complex":
        real = (self.real * no.real + self.imaginary * no.imaginary) / (math.pow(no.real, 2) + math.pow(no.imaginary, 2))
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (math.pow(no.real, 2) + math.pow(no.imaginary, 2))

        return Complex(real, imaginary)

    def mod(self) -> "Complex":
        """Returns the modulus of the complex number"""
        real = math.pow(self.real**2 + self.imaginary**2, 0.5)
        imaginary = 0
        return Complex(real, imaginary)

    def __str__(self) -> str:
        if self.imaginary == 0:
            result = f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                result = f"0.00+{self.imaginary:.2f}i"
            else:
                result = f"0.00-{abs(self.imaginary):.2f}i"
        elif self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{abs(self.imaginary):.2f}i"

        return result


def main() -> None:
    """Main function"""
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep="\n")


if __name__ == "__main__":
    main()

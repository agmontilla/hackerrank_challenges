""" Reduce Function Challenge. """
from fractions import Fraction
from functools import reduce


def product(fracs: list[Fraction]) -> tuple[int, int]:
    """Return the product of the fractions."""
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


def main() -> None:
    """Main function."""
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))

    result = product(fracs)
    print(*result)


if __name__ == "__main__":
    main()

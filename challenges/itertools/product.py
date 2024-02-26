""" Show how to use itertools.product to get the cartesian product of two lists. """

from itertools import product


def run_product(a: list[int], b: list[int]) -> list[tuple[int, int]]:
    """Return the cartesian product of a and b."""
    return list(product(a, b))


def main() -> None:
    """Main function"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = run_product(a, b)

    print(*result)


if __name__ == "__main__":
    main()

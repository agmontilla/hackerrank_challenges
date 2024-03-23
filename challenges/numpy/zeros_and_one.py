""" Zeros and Ones Challenge """
import numpy as np


def generate_zeros(dimn: tuple[int, ...]) -> np.ndarray:
    """Generate an array of zeros"""
    return np.zeros(dimn, dtype=int)


def generate_ones(dimn: tuple[int, ...]) -> np.ndarray:
    """Generate an array of ones"""
    return np.ones(dimn, dtype=int)


def main() -> None:
    """Main function"""
    dimn = tuple(map(int, input().strip().split()))
    print(generate_zeros(dimn))
    print(generate_ones(dimn))


if __name__ == "__main__":
    main()

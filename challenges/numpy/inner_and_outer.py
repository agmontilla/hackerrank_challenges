""" Inner and Outer Challenge """
from typing import Any

import numpy as np


def get_entries() -> tuple[list[int], list[int]]:
    """Getting inputs from user"""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return a, b


def apply_inner_outer(a: list[int], b: list[int]) -> tuple[Any, np.ndarray]:
    """Applying inner and outer operations to two arrays"""
    arr_a, arr_b = np.array(a), np.array(b)
    return np.inner(arr_a, arr_b), np.outer(arr_a, arr_b)


def main() -> None:
    """Main function"""
    result = apply_inner_outer(*get_entries())
    print(*result, sep="\n")


if __name__ == "__main__":
    main()

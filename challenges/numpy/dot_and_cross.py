""" Dot and Cross Challenge """
from typing import Any

import numpy as np


def get_entries() -> tuple[list[list[int]], list[list[int]]]:
    """Getting inputs from user"""
    n = int(input())
    a = [list(map(int, input().split()))[:n] for _ in range(n)]
    b = [list(map(int, input().split()))[:n] for _ in range(n)]
    return a, b


def apply_dot_operation(a: list[list[int]], b: list[list[int]]) -> Any:
    """Appliyng dot operation to two arrays"""
    arr_a, arr_b = np.array(a), np.array(b)
    return np.dot(arr_a, arr_b)


def main() -> None:
    """Main function"""
    result = apply_dot_operation(*get_entries())
    print(result)


if __name__ == "__main__":
    main()

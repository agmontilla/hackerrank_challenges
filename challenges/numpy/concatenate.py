"""Concatenate Challenge"""
import numpy as np


def build_array(arr: list[list[str]]) -> np.ndarray:
    """Build an array"""
    return np.array(arr, dtype=int)


def read_array(rows: int, columns: int) -> list[list[str]]:
    """Read an array"""
    return [input().split(" ")[:columns] for _ in range(rows)]


def main() -> None:
    """Main function"""
    n, m, p = map(int, input().strip().split(" "))
    arr1 = read_array(n, p)
    arr2 = read_array(m, p)
    print(np.concatenate((np.array(arr1, dtype=int), np.array(arr2, dtype=int))))
    # print(np.concatenate((build_array(n, p), build_array(m, p))))


if __name__ == "__main__":
    main()

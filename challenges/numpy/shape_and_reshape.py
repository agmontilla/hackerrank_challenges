""" Shape and Reshape Challenge """
import numpy as np


def arrays(arr: list[str]) -> np.ndarray:
    """Set every element to int and reshape the array"""
    return np.array(arr, dtype=int).reshape(3, 3)


def main() -> None:
    """Main function"""
    arr = input().strip().split(" ")
    result = arrays(arr)
    print(result)


if __name__ == "__main__":
    main()

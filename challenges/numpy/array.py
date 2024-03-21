""" Arrays Challenge """
import numpy as np


def arrays(arr: list[str]) -> np.ndarray:
    """Set every element to float and reverse the array"""
    reverse = np.array(arr, dtype=float)[::-1]
    return reverse


def main() -> None:
    """Main function"""
    arr = input().strip().split(" ")
    result = arrays(arr)
    print(result)


if __name__ == "__main__":
    main()

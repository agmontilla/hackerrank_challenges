""" Min and Max Challenge """
import numpy as np

from challenges.numpy.utils import get_entries


def min_max(data: list[list[int]]) -> int:
    """Appliyng min and max operations on data"""

    arr = np.array(data)
    return int(np.max(np.min(arr, axis=1)))


def main() -> None:
    """Main function"""
    result = min_max(get_entries())
    print(result)


if __name__ == "__main__":
    main()

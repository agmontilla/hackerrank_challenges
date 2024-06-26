""" Sum and Prod Challenge """
import numpy as np

from challenges.numpy.utils import get_entries


def perform_operations(data: list[list[int]]) -> int:
    """Perform sum and prod operation"""
    arr = np.array(data)
    return int(np.prod(np.sum(arr, axis=0)))


def main() -> None:
    """Main function"""
    result = perform_operations(get_entries())
    print(result)


if __name__ == "__main__":
    main()

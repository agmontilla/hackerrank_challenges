""" Floor Ceil and Rint Challenge """
from typing import Generator

import numpy as np

OPERATIONS = ("floor", "ceil", "rint")


def apply_operations(arr: np.ndarray) -> Generator[np.ndarray, None, None]:
    """Apply operations to an array"""
    for operation in OPERATIONS:
        yield (getattr(np, operation)(arr))


def main() -> None:
    """Main function"""
    arr = np.array(list(map(float, input().strip().split())))
    np.set_printoptions(legacy="1.13")
    print(*apply_operations(arr), sep="\n")


if __name__ == "__main__":
    main()

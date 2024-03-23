""" Transpose and Flatten Challenge """
import numpy as np


def get_transpose_and_flatten(arr: list[list[str]]) -> tuple[np.ndarray, np.ndarray]:
    """Get the transpose and flatten of the matrix"""
    matrix = np.array(arr, dtype=int)
    return matrix.transpose(), matrix.flatten()


def main() -> None:
    """Main function"""
    n, m = map(int, input().strip().split(" "))
    data = [input().split(" ")[:m] for _ in range(n)]
    print(*get_transpose_and_flatten(data), sep="\n")


if __name__ == "__main__":
    main()

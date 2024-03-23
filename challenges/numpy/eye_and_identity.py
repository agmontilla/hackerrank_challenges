""" Eye and Identity Challenge """
import numpy as np


def generate_eye(rows: int, columns: int) -> np.ndarray:
    """Generate an identity array"""
    result: np.ndarray = np.eye(rows, columns, k=0)
    return result


def main() -> None:
    """Main function"""
    np.set_printoptions(legacy="1.13")
    n, m = tuple(map(int, input().strip().split()))
    print(generate_eye(n, m))


if __name__ == "__main__":
    main()

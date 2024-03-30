""" Linear Algebra Challenge """
import numpy as np


def get_entries() -> list[list[float]]:
    """Getting inputs from user"""

    n = int(input())
    matriz = [list(map(float, input().split())) for _ in range(n)]

    return matriz


def calculate_det(target: list[list[float]]) -> float:
    """Calculate the determinant of a matrix"""
    return float(np.linalg.det(np.array(target)))


def main() -> None:
    """Main function"""
    result = calculate_det(get_entries())
    print(f"{result:.2}")


if __name__ == "__main__":
    main()

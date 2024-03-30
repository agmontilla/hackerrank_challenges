""" Polynomial Challenge """
import numpy as np
import numpy.typing as npt


def get_entries() -> tuple[list[float], int]:
    """Getting inputs from user"""
    coef = list(map(float, input().split()))
    target = int(input())
    return (coef, target)


def apply_polynomial_operation(coef: list[float], value: int) -> npt.NDArray:
    """Evaluate a polynomial at a specific value"""
    return np.polyval(coef, value)


def main() -> None:
    """Main function"""
    result = apply_polynomial_operation(*get_entries())
    print(result)


if __name__ == "__main__":
    main()

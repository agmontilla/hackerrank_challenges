import numpy as np

OPERATIONS = ("add", "subtract", "multiply", "divide", "mod", "power")
TOTAL_AMOUNT_OF_ARRAYS = 2


def apply_operations(a: list[np.ndarray], b: list[np.ndarray]) -> list[np.ndarray]:
    """Apply operations to two arrays"""
    return [np.array(getattr(np, operation)(a, b), dtype=int) for operation in OPERATIONS]


def main() -> None:
    """Main function"""
    n, m = tuple(map(int, input().strip().split()))
    a, b = [[np.array(input().split(), dtype=int)[:m] for _ in range(n)] for _ in range(2)]

    print(*apply_operations(a, b), sep="\n")


if __name__ == "__main__":
    main()

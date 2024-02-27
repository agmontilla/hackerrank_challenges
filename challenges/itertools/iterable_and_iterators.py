""" Iterable and Iterators Challenge. """
from itertools import combinations


def find_probability(s: list[str], k: int) -> float:
    """Find the probability of the combination."""
    cont = 0
    max_idx = 0

    for idx, comb in enumerate(combinations(s, k)):
        max_idx = idx
        if "a" in comb:
            cont += 1

    return cont / (float(max_idx) + 1)


def main() -> None:
    """Main function."""

    n = input()
    s = list(input().split())[: int(n)]
    k = int(input())

    print(f"{find_probability(s, k):.4f}")


if __name__ == "__main__":
    main()

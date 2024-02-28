""" Default Dict Challenge """
from collections import defaultdict
from typing import DefaultDict


def total_per_letter(n: int, m: int, all_positions: DefaultDict) -> list:
    """Get the total of positions for each letter"""

    for idx in range(n):
        ch = input()
        all_positions[ch] = all_positions[ch] + " " + str(idx + 1) if ch in all_positions else str(idx + 1)

    data = [all_positions[ch] for ch in [input() for _ in range(m)]]

    return data


def main() -> None:
    """Main function"""
    n, m = input().split()
    all_positions: DefaultDict = defaultdict(lambda: -1)

    results = total_per_letter(int(n), int(m), all_positions)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()

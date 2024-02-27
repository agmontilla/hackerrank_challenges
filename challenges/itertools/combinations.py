""" Combinations Challenge """

from itertools import combinations


def run_combinations(times: int, substr: str) -> list[str]:
    """Run combinations and return the list of combinations."""
    data = ["".join(combn) for i in range(1, int(times) + 1) for combn in combinations(sorted(substr), i)]
    return data


def main() -> None:
    """Main function."""
    substr, times = input().split()
    data = run_combinations(int(times), substr)
    print(*data, sep="\n")


if __name__ == "__main__":
    main()

""" Combinations with Replacement Challenge """
from itertools import combinations_with_replacement


def run_combinations_with_replacement(times: int, substr: str) -> list[str]:
    """Run combinations with replacement and return the list of combinations with replacement."""
    data = ["".join(permut) for permut in combinations_with_replacement(sorted(substr), int(times))]
    return data


def main() -> None:
    """Main function."""
    substr, times = input().split()

    data = run_combinations_with_replacement(int(times), substr)

    print(*data, sep="\n")


if __name__ == "__main__":
    main()
    # substr, times = input().split()

    # print(*["".join(permut) for permut in combinations_with_replacement(sorted(substr), int(times))], sep="\n")

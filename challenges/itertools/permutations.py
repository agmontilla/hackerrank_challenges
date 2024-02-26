""" Itertools Permutation Challenge """

from itertools import permutations


def run_permutations(substr: str, times: int) -> list[str]:
    """Return the permutations of substr with length times."""
    output = []
    for permut in permutations(sorted(substr), times):
        output.append("".join(permut))

    return output


def main() -> None:
    """Main function"""
    substr, t_ = input().split()
    times = int(t_)

    results = run_permutations(substr, times)

    print("\n".join(results))


if __name__ == "__main__":
    main()

""" Maximize It! Challenge """
from itertools import product


def maximize_it(remain_number: str, coefs: list[list[int]]) -> int:
    """Find the maximum value of the expression."""

    k2 = [sum(pow(value, 2) for value in poss) % int(remain_number) for poss in product(*coefs)]
    return int(max(k2))


def main() -> None:
    """Main function."""

    entries, remain_number = input().split()
    coefs = [list(map(int, input().split()))[1:] for _ in range(int(entries))]

    print(f"{maximize_it(remain_number, coefs)}")


if __name__ == "__main__":
    main()

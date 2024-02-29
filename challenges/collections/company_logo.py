""" Company Logo Challenge """
from collections import Counter


def most_common(s: str) -> Counter[str]:
    """Main function"""
    count = Counter(sorted(s))
    return count


def main() -> None:
    """Main function"""
    s = input()

    result = most_common(s)

    print(*(f"{k} {v}" for k, v in result.most_common(3)), sep="\n")


if __name__ == "__main__":
    main()

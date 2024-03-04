""" Incorrect Regex Challenge """
import re


def is_valid_regex(regex: str) -> bool:
    """Returns True if the regex is valid, False otherwise"""
    try:
        re.compile(regex)
        return True
    except Exception:  # pylint: disable=broad-except
        return False


def main() -> None:
    """Main function"""
    results = []

    for _ in range(int(input())):
        results.append(is_valid_regex(input()))

    print(*results, sep="\n")


if __name__ == "__main__":
    main()

""" Detect Floating Point Number Challenge """

import re

PATTERN = re.compile("(^[+.-]{0,1}[0-9]{0,}[.][0-9]{1,}$)")


def is_float(s: str) -> bool:
    """Return True if the string is a floating point number.
    Otherwise, return False.
    """
    return PATTERN.search(s) is not None


def main() -> None:
    """Main function."""
    cases = [is_float(input()) for _ in range(int(input()))]
    print(*cases, sep="\n")


if __name__ == "__main__":
    main()

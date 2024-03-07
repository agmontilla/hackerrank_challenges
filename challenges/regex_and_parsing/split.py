""" Split Challenge.
Consists of splitting a string by the characters "." and ",".
"""

import re

REGEX_PATTERN = r"[.,]"


def main() -> None:
    """Main function."""
    print("\n".join(re.split(REGEX_PATTERN, input())))


if __name__ == "__main__":
    main()

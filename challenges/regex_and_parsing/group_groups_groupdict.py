""" Group(), Groups() & Groupdict() Challenge """
import re

PATTERN = re.compile(r"([a-zA-Z0-9])\1+")


def main() -> None:
    """Main function."""
    m = PATTERN.search(input())
    print(m.groups()[0] if m else -1)


if __name__ == "__main__":
    main()

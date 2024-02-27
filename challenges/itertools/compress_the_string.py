""" Compress the String! """
from itertools import groupby


def compress_the_string(substr: str) -> list[tuple[int, int]]:
    """Compress the string and return the list of tuples."""
    return [(len(list(g)), int(k)) for k, g in groupby(substr)]


def main() -> None:
    """Main function."""
    substr = input()
    data = compress_the_string(substr)
    print(*data)


if __name__ == "__main__":
    main()

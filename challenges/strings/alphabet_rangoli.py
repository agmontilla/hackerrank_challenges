""" Alphabet Rangoli """

import string


def print_rangoli(size: int) -> None:
    """Print the rangoli"""
    chs = string.ascii_lowercase[:size]

    for i in range(-size + 1, size):
        i = abs(i)
        dashes = "-" * (2 * i)
        letters = "-".join(chs[:i:-1] + chs[i:])
        print(dashes + letters + dashes)


def main() -> None:
    """Main function"""
    n = int(input())
    print_rangoli(n)


if __name__ == "__main__":
    main()

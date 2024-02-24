""" Text Wrap """

import textwrap


def wrap(string: str, max_width: int) -> str:
    """Wrap the string"""
    return textwrap.fill(string, max_width)


def main() -> None:
    """Main function"""
    string = input()
    max_width = int(input())
    print(wrap(string, max_width))


if __name__ == "__main__":
    main()

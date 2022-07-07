import textwrap


def wrap(string: str, max_width: int) -> str:
    return textwrap.fill(string, max_width)


def main() -> None:
    string = input()
    max_width = int(input())
    print(wrap(string, max_width))


if __name__ == "__main__":
    main()

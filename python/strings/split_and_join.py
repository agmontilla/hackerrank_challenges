""" Split and Join """


def split_and_join(line: str) -> str:
    """Split and join the string"""
    return "-".join(line.split(" "))


def main() -> None:
    """Main function"""
    line = input()
    print(split_and_join(line))


if __name__ == "__main__":
    main()

def split_and_join(line: str) -> str:
    return '-'.join(line.split(' '))


def main() -> None:
    line = input()
    print(split_and_join(line))


if __name__ == '__main__':
    main()

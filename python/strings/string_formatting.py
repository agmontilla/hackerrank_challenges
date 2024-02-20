""" String Formatting """


def print_formatted(number: int) -> None:
    """ Print the formatted string """
    width = len(f'{number:b}')

    for i in range(1, number+1):
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')


def main() -> None:
    """ Main function """
    n = int(input())
    print_formatted(n)


if __name__ == "__main__":
    main()

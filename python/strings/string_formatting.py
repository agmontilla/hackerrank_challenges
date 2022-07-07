def print_formatted(number: int) -> None:
    width = len(f'{number:b}')

    for i in range(1, number+1):
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')


def main() -> None:
    n = int(input())
    print_formatted(n)


if __name__ == "__main__":
    main()

# Enter your code here. Read input from STDIN. Print output to STDOUT

def add(countries_number: int) -> None:
    countries = {input('') for _ in range(countries_number)}
    print(countries.__len__())


def main() -> None:
    countries_number = int(input(''))
    add(countries_number)


if __name__ == '__main__':
    main()

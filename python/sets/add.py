# Enter your code here. Read input from STDIN. Print output to STDOUT
""" You have to write a program that reads a list of country names from input and then prints the total number of distinct countries.
    The input will contain the number of countries in the first line, and then a list of country names.
    The country names might have spaces in them.
"""


def add(countries_number: int) -> None:
    """ Add countries to a set and print the number of distinct countries """
    countries = {input('') for _ in range(countries_number)}
    print(len(countries))


def main() -> None:
    """ Main function """
    countries_number = int(input(''))
    add(countries_number)


if __name__ == '__main__':
    main()

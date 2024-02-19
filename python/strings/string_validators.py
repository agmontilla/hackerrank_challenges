""" String Validators """


def check_string(string: str) -> None:
    """ Check the string """
    functions = [str.isalnum, str.isalpha,
                 str.isdigit, str.islower, str.isupper]

    for func in functions:
        print(any(func(ch) for ch in string))


def main() -> None:
    """ Main function """
    string = input()
    check_string(string)


if __name__ == '__main__':
    main()

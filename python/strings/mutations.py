""" Mutations """


def mutate_string(string: str, position: int, character: str) -> str:
    """ Mutate the string """
    return string[:position] + character + string[position + 1:]


def main() -> None:
    """ Main function """
    s = input()
    i, c = input().split()
    print(mutate_string(s, int(i), c))


if __name__ == "__main__":
    main()

""" Swap Case """


def swap_case(s: str) -> str:
    """ Swap the case of the string """
    characters = [ch.lower() if ch.isupper() else ch.upper() for ch in s]
    return ''.join(characters)


def main() -> None:
    """ Main function """
    sample = input()
    print(swap_case(sample))


if __name__ == "__main__":
    main()

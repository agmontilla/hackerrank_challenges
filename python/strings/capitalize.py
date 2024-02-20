# Complete the solve function below.
""" Capitalize! """


def solve(s: str) -> str:
    """ Capitalize the first letter of each word in the string. """
    new_words = list(map(str.capitalize, s.split()))
    old_words = s.split()
    for new_word, old_word in zip(new_words, old_words):
        s = s.replace(old_word, new_word)

    return s


def main() -> None:
    """ Main function """
    print(solve(input()))


if __name__ == '__main__':
    main()

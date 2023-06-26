# Complete the solve function below.

def solve(s: str) -> str:
    new_words = list(map(str.capitalize, s.split()))
    old_words = s.split()
    for new_word, old_word in zip(new_words, old_words):
        s = s.replace(old_word, new_word)

    return s


def main() -> None:
    print(solve(input()))


if __name__ == '__main__':
    main()

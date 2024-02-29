""" Word Order Challenge """

from collections import OrderedDict


def get_counting_words(words: list[str]) -> dict:
    """Get the counting of words"""
    counting_words: dict = OrderedDict()
    for word in words:
        counting_words[word] = counting_words.get(word, 0) + 1

    return counting_words


def main() -> None:
    """Main function"""
    lines = int(input())
    words = [input() for _ in range(lines)]

    result = get_counting_words(words)

    print(len(result))
    print(*result.values())


if __name__ == "__main__":
    main()

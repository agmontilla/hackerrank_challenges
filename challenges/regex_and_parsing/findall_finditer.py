""" FindAll and FindIter Challenge
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
"""

import re
import string


def _get_consonants(vowels: str) -> str:
    """Get consonants"""
    return "".join(ch for ch in string.ascii_lowercase if ch not in vowels)


class FindVowels:
    """FindVowels class"""

    VOWELS = "aeiou"
    CONSONANT = _get_consonants(VOWELS)
    PATTERN = re.compile(
        "(?<=[{c}])([{v}]{{2,}}(?=[{c}]))".format(c=CONSONANT, v=VOWELS),
        flags=re.IGNORECASE,
    )

    def __init__(self, s: str):
        self.sentence = s

    def run(self) -> None:
        """Find all the substrings of that contains vowels"""
        match = re.findall(self.PATTERN, self.sentence)
        print(*match if match else [-1], sep="\n")


def main() -> None:
    """Main function"""
    sentence = input()
    FindVowels(sentence).run()


if __name__ == "__main__":
    main()

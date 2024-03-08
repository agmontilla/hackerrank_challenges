""" Start and End Challenge """

import re


class StartEnd:
    """Start and End class"""

    OUTPUT_FORMAT = "({}, {})"

    def __init__(self, s: str, k: str):
        self.sentence = s
        self.k = k

    def get_indexes(self) -> list[str]:
        """Find the start and end index of the substring in the string"""
        indexes = []

        match = re.finditer(f"(?={self.k})", self.sentence)
        for m in match:
            indexes.append(self.OUTPUT_FORMAT.format(m.start(), m.start() + len(self.k) - 1))

        return indexes or [self.OUTPUT_FORMAT.format(-1, -1)]


def main() -> None:
    """Main function"""
    sentence = input()
    k = input()

    indexes = StartEnd(sentence, k).get_indexes()

    print(*indexes, sep="\n")


if __name__ == "__main__":
    main()

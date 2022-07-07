from typing import Generator


class MergeTheTools:
    def __init__(self, s: str, k: int):

        if not self._is_factor(len(s), k):
            raise ValueError("K is not a factor of length of the string")

        self.sentence = s
        self.k = k

    def run(self) -> None:
        for substring in self._substrings_generator():
            print("".join(dict.fromkeys(substring).keys()))

    def _substrings_generator(self) -> Generator[str, None, None]:
        amount_of_substrings = len(self.sentence) // self.k

        for i in range(amount_of_substrings):
            start, end = i * self.k, (i + 1) * self.k
            yield self.sentence[start:end]

    def _is_factor(self, length: int, k: int) -> bool:
        return True if length % k == 0 else False


def merge_the_tools(string: str, k: int) -> None:
    MergeTheTools(string, k).run()


def main() -> None:
    string = input()
    k = int(input())
    merge_the_tools(string, int(k))


if __name__ == "__main__":
    main()

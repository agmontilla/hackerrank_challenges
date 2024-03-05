""" Ginorts Challenge """


class InverseSort:
    """Inverse Sort"""

    def __init__(self, s: str):
        self.s = s

    def _lowercase_sorted(self) -> str:
        return "".join(sorted([ch for ch in self.s if ch.islower()]))

    def _uppercase_sorted(self) -> str:
        return "".join(sorted([ch for ch in self.s if ch.isupper()]))

    def _split_digits(self) -> tuple[tuple[str, ...], tuple[str, ...]]:
        """Split the digits in two tuples: even and odd"""
        digits = [ch for ch in self.s if ch.isdigit()]
        even = tuple(filter(lambda x: int(x) % 2 == 0, digits))
        odd = tuple(filter(lambda x: int(x) % 2 != 0, digits))

        return even, odd

    def _digits_sorted(self) -> str:
        even, odd = self._split_digits()
        return "".join(sorted(odd) + sorted(even))

    def custom_sorted(self) -> str:
        """Sort the string in the following order:
        1. Lowercase
        2. Uppercase
        3. Odd digits
        4. Even digits
        """
        return f"{self._lowercase_sorted()}{self._uppercase_sorted()}{self._digits_sorted()}"


def main() -> None:
    """Main function"""
    sentence = input()
    expression = InverseSort(sentence)
    print(expression.custom_sorted())


if __name__ == "__main__":
    main()

# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Integers Come In All Sizes """


class IntegersComeInAllSizes:
    """A class to get the sum of the powers of integers."""

    @staticmethod
    def get_integers_come_in_all_sizes(a: int, b: int, c: int, d: int) -> None:
        """A function to get the sum of the powers of integers."""
        print(f"{pow(a, b) + pow(c, d)}")


def main() -> None:
    """The main function to get the input and print the output."""
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    IntegersComeInAllSizes.get_integers_come_in_all_sizes(a, b, c, d)


if __name__ == "__main__":
    main()

# Enter your code here. Read input from STDIN. Print output to STDOUT

class IntegersComeInAllSizes:
    @staticmethod
    def get_integers_come_in_all_sizes(a: int, b: int, c: int, d: int) -> None:
        print(f'{pow(a, b) + pow(c, d)}')


def main() -> None:
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    IntegersComeInAllSizes.get_integers_come_in_all_sizes(a, b, c, d)


if __name__ == "__main__":
    main()

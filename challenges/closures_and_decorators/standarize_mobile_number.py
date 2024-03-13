""" Standarize Mobile Number Using Decorators Challenge """

from typing import Callable


def wrapper(f: Callable) -> Callable:
    """Wrapper function"""

    def fun(phone_numbers: list[str]) -> None:
        """Inner function"""

        def formating_strings(data: str, n: int) -> str:
            return " ".join([data[s : s + n] for s in range(0, len(data), n)])

        f(f"+91 {formating_strings(num[len(num) - 10:] if len(num) > 10 else num, 5)}" for num in phone_numbers)

    return fun


@wrapper
def sort_phone(phone_numbers: list[str]) -> None:
    """Sort the phone numbers"""
    print(*sorted(phone_numbers), sep="\n")


def main() -> None:
    """Main functions"""
    phone_numbers = [input() for _ in range(int(input()))]
    sort_phone(phone_numbers)


if __name__ == "__main__":
    main()

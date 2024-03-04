""" Exception Challenge """

from typing import Any, Union


def perform_division(a: Any, b: Any) -> Union[int, str]:
    """Returns the result of a division"""
    try:
        return int(a) // int(b)
    except (ZeroDivisionError, ValueError) as e:
        return f"Error Code: {str(e)}"


def main() -> None:
    """Main function"""
    results = []

    for _ in range(int(input())):
        a, b = input().split()
        results.append(perform_division(a, b))

    print(*results, sep="\n")


if __name__ == "__main__":
    main()

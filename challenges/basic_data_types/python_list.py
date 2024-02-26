""" Python List """
from typing import Any, List


def run_option(option: str, collection: List, args: Any) -> None:
    """Run the option on the collection"""

    options = ["insert", "print", "remove", "append", "sort", "pop", "reverse", "print"]

    if option not in options:
        raise ValueError("This option is not valid")

    if option == "print":
        print(collection)
    else:
        getattr(collection, option)(*args)


def main() -> None:
    """Main function"""
    n = int(input())
    data: List = []
    for _ in range(n):
        opt, *line = input().split()
        arguments = list(map(int, line))
        run_option(opt, data, arguments)


if __name__ == "__main__":
    main()

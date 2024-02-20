""" Discard, Remove, Pop """
from typing import Set


def run_discard_remove_pop(s: Set, operations: int) -> Set:
    """ Execute operations """
    while operations > 0:
        func, *args = input().split()
        getattr(s, func)(*map(int, args))
        operations -= 1

    return s


def main() -> None:
    """ Main method """
    n = int(input())
    s = set(map(int, input().split()[:n]))
    operations_number = int(input())

    print(f'{sum(run_discard_remove_pop(s, operations_number))}')


if __name__ == "__main__":
    main()

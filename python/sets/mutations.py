# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Mutations """
from typing import Set


def run_mutations(set_x: Set, operations: int) -> int:
    """ Run Mutations """
    for _1 in range(operations):
        func, members_total = input().split()
        set_tmp = set(list(map(int, input().split()))[:int(members_total)])

        getattr(set_x, func)(set_tmp)

    return sum(set_x)


def main() -> None:
    """ Main Function """
    _ = int(input())
    set_a = set(map(int, input().split()))
    total_operations = int(input())

    print(f'{run_mutations(set_a, total_operations)}')


if __name__ == "__main__":
    main()

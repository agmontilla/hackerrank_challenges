# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .intersection() Operation """
from typing import Set


def run_intersection(set_a: Set, set_b: Set) -> int:
    """ Run set intersection function """
    total = len(set_a.intersection(set_b))
    return total


def main() -> None:
    """ Main function """
    _ = int(input())
    english_students = set(map(int, input().split()))
    _ = int(input())
    french_students = set(map(int, input().split()))

    students_total = run_intersection(english_students, french_students)

    print(f'{students_total}')


if __name__ == "__main__":
    main()

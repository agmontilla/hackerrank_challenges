# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .difference() Operation """
# pylint: disable=duplicate-code
from typing import Set


def run_difference(set_a: Set, set_b: Set) -> int:
    """Find the difference between two sets"""
    total = len(set_a.difference(set_b))
    return total


def main() -> None:
    """Main function"""
    _ = int(input())
    english_students = set(map(int, input().split()))
    _ = int(input())
    french_students = set(map(int, input().split()))

    print(run_difference(english_students, french_students))


if __name__ == "__main__":
    main()

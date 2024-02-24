# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .symmetric_difference() Operation """
# pylint: disable=duplicate-code


def get_symetric_difference(set_a: set, set_b: set) -> int:
    """Get the symmetric difference"""
    total = len(set_a.symmetric_difference(set_b))
    return total


def main() -> None:
    """Main function"""
    _ = int(input())
    english_students = set(map(int, input().split()))
    _ = int(input())
    french_students = set(map(int, input().split()))

    students_total = get_symetric_difference(english_students, french_students)

    print(f"{students_total}")


if __name__ == "__main__":
    main()

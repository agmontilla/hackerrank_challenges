# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .union() Operation """


def run_union(set_a: set, set_b: set) -> int:
    """Run Union"""
    return len(set_a.union(set_b))


def main() -> None:
    """Main function"""
    n1 = int(input())
    english_students = set(list(map(int, input().split()))[:n1])
    n2 = int(input())
    french_students = set(list(map(int, input().split()))[:n2])

    students_total = run_union(english_students, french_students)

    print(f"{students_total}")


if __name__ == "__main__":
    main()

# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Check Subset """


def check_subset() -> None:
    """Check if the first set is a subset of the second set"""
    test_cases = int(input())

    sets = [(int(input()), set(input().split())) for _ in range(test_cases) for _ in range(2)]

    for i in range(0, 2 * test_cases, 2):
        print(sets[i][1].issubset(sets[i + 1][1]))


def main() -> None:
    """Main function"""
    check_subset()


if __name__ == "__main__":
    main()

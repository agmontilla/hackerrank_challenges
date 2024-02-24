# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Check Strict Superset """


def check_strict_superset() -> bool:
    """Check Strict Superset"""

    set_a = set(input().split())

    checks = [set_a.issuperset(set(input().split())) for _ in range(int(input()))]

    return all(checks)


def main() -> None:
    """Main Function"""
    print(check_strict_superset())


if __name__ == "__main__":
    main()

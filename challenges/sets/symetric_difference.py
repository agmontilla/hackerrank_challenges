# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Symmetric Difference (in a manual way)"""


def run_symetric_difference(sets: list[list[int]]) -> list[int]:
    """Run Symmetric Difference"""

    unique = []

    for x_pos, x in enumerate(sets):
        for y_pos, y in enumerate(sets):
            if x_pos != y_pos:
                unique.extend(list(set(x).difference(set(y))))

    return sorted(unique)


def main() -> None:
    """Main function"""
    sets = []

    for _ in range(2):
        n = int(input())
        sets.append(list(map(int, input().split()))[:n])

    results = run_symetric_difference(sets)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()

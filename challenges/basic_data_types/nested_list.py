""" Nested List """
from typing import List


def get_second_lowest_grade(data: List[List]) -> List[str]:
    """Get the second lowest grade from a list of lists."""
    scores = sorted(list({score for _, score in data}))
    second_lowest_grade = scores[1]
    names = sorted([name for name, score in data if score == second_lowest_grade])

    return names


def main() -> None:
    """Main function."""
    data: List[List] = [[input(), float(input())] for _ in range(int(input()))]
    names = get_second_lowest_grade(data)
    print(*names, sep="\n")


if __name__ == "__main__":
    main()

"""" Find the second max number in a list """
from typing import Any, List


def get_runner_up(_: Any, all_scores: List[int]) -> int:
    """Get the second max number in a list"""

    ordered_scores = sorted(all_scores)

    pos_max = ordered_scores.index(max(ordered_scores))

    runner_up = ordered_scores[pos_max - 1]

    return runner_up


def main() -> None:
    """Main function"""
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_runner_up(n, arr))


if __name__ == "__main__":
    main()

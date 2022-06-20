def get_runner_up(possible_runner_up: int, all_scores: map[int]) -> int:
    # TODO: possible_runner_up is not used in this function. Remove it.

    ordered_scores = sorted(all_scores)

    pos_max = ordered_scores.index(max(ordered_scores))

    runner_up = ordered_scores[pos_max - 1]

    return runner_up


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    print(get_runner_up(n, arr))

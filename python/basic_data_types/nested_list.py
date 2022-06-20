from typing import List

if __name__ == "__main__":
    data: List[List] = [[input(), float(input())] for _ in range(int(input()))]

    scores = sorted(list(set([score for _, score in data])))
    second_lowest_grade = scores[1]
    names = sorted([name for name, score in data if score == second_lowest_grade])
    print(*names, sep="\n")

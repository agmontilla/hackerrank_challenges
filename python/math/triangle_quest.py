""" Triangle Quest
    for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(int(i*(pow(10, i)-1)/9))
"""


class TriangleQuest:

    @staticmethod
    def triangle_quest(n: int) -> None:
        for i in range(1, n):
            print(int(i * (pow(10, i) - 1) / 9))


def main() -> None:
    TriangleQuest.triangle_quest(int(input()))


if __name__ == "__main__":
    main()

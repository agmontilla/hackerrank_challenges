

class TriangleQuest2:

    @staticmethod
    def get_triangle_quest2(n: int) -> None:
        for i in range(1, n+1):
            print(int(pow((pow(10, i)-1)//9, 2)))


def main() -> None:
    n = int(input())
    triangle_quest2 = TriangleQuest2()
    triangle_quest2.get_triangle_quest2(n)


if __name__ == "__main__":
    main()

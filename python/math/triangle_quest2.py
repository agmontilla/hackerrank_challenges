""" Triangle Quest 2 """


class TriangleQuest2:
    """ Class for Triangle Quest 2 """

    @staticmethod
    def get_triangle_quest2(n: int) -> None:
        """ Get Triangle Quest 2 """
        for i in range(1, n+1):
            print(int(pow((pow(10, i)-1)//9, 2)))


def main() -> None:
    """ Main function """
    n = int(input())
    triangle_quest2 = TriangleQuest2()
    triangle_quest2.get_triangle_quest2(n)


if __name__ == "__main__":
    main()

""" Pilling Up Challenge """


class Cube:
    """Cube class"""

    length: int
    elements: list[int]

    def __init__(self, length: int) -> None:
        self.length = length

    def set_elements(self) -> None:
        """Set elements of the cube"""
        self.elements = list(map(int, input().split()))[: self.length]

    def is_pileable(self) -> str:
        """Check if the cubes can be piled up"""
        middle = self.elements.index(min(self.elements))

        left_cubes = self.elements[:middle]
        right_cubes = self.elements[middle + 1 :]

        if left_cubes == sorted(left_cubes, reverse=True) and right_cubes == sorted(right_cubes):
            return "Yes"

        return "No"


def main() -> None:
    """Main function"""

    answers = []

    for _ in range(int(input())):
        n = int(input())
        cube = Cube(n)
        cube.set_elements()
        answers.append(cube.is_pileable())

    print(*answers, sep="\n")


if __name__ == "__main__":
    main()

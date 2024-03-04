""" Find the Torsional Angle Challenge"""
import math


class Points:
    """Class to save a point in 3D space and perform operations with it"""

    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no: "Points") -> "Points":
        return Points(no.x - self.x, no.y - self.y, no.z - self.z)

    def dot(self, no: "Points") -> float:
        """Returns the dot product of two points"""
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no: "Points") -> "Points":
        """Returns the cross product of two points"""
        i = self.y * no.z - self.z * no.y
        j = -1 * (self.x * no.z - self.z * no.x)
        k = self.x * no.y - self.y * no.x
        return Points(i, j, k)

    def absolute(self) -> float:
        """Returns the absolute value of the point"""
        return float(pow((self.x**2 + self.y**2 + self.z**2), 0.5))

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"


def main() -> None:
    """Main function"""
    points = []
    for _ in range(4):
        elements = list(map(float, input().split()))
        points.append(elements)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print(f"{math.degrees(angle):.2f}")


if __name__ == "__main__":
    main()
